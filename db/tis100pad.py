# -*- coding: utf-8 -*-

from flask import Flask, request, g, json, make_response
from logging import FileHandler
from random import randint
from os import mkdir
import definitions
import sqlite3

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10240
app.logger.addHandler(FileHandler(definitions.logfile))
DATABASE = definitions.database


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(e):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/submit', methods=['POST'])
def submit_solution():
    db = get_db()
    master = int(request.form['master']) if int(request.form['master']) else None
    if master:
        currentfork = db.execute('SELECT forkno FROM solutions WHERE master=? ORDER BY forkno DESC', (master,)).fetchone()
        currentfork = currentfork[0] if currentfork else 0
    else:
        currentfork = None
    forkno = currentfork + 1 if currentfork is not None else None
    levelcode = request.form['levelcode'] if request.form['levelcode'] else None
    ports = request.form['ports']
    row = (master, forkno,
           request.form['@0'], request.form['@1'], request.form['@2'], request.form['@3'], 
           request.form['@4'], request.form['@5'], request.form['@6'], request.form['@7'], 
           request.form['@8'], request.form['@9'], request.form['@10'], request.form['@11'],
           ports, levelcode)
    if currentfork:
        if row[2:14] == db.execute('SELECT * FROM solutions WHERE master=? AND forkno=?', (master, currentfork)).fetchone()[2:14]:
            return ('No changes.', 202)
    elif master:
        if row[2:14] == db.execute('SELECT * FROM solutions WHERE rowid=?',(master,)).fetchone()[2:14]:
            return ('No changes.', 202)           
    newrow = db.execute('INSERT INTO solutions VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row).lastrowid
    db.commit()
    return str(newrow if not forkno else master) + '/' + str(forkno if forkno else 0)


@app.route('/upload', methods=['POST'])
def upload_save():
    file = request.files['file']
    levelcode = file.filename.split('.')[0]
    if levelcode not in definitions.levels:
        return ('Invalid file.', 400)
    entries = file.read().replace('\r', '').split('@')
    entries.pop(0)
    text = ['', '', '', '', '', '', '', '', '', '', '', '']
    for i in range(0, 12):
        if definitions.levels[levelcode][i] == 1:
            text[i] = definitions.stcknode
        if definitions.levels[levelcode][i] == 2:
            text[i] = definitions.errnode
    for entry in entries:
        text[text.index('')] = entry[entry.find('\n'):]
    textfields = dict()
    textfields['ports'] = definitions.levels[levelcode][12]
    textfields['levelname'] = definitions.levels[levelcode][13]
    textfields['levelcode'] = levelcode
    for i in range (0, 12):
        textfields['@' + str(i)] = text[i]
    return json.dumps(textfields)


@app.route('/download', methods=['POST'])
def produce_file():
    levelcode = request.form['levelcode'] if request.form['levelcode'] else 'level'
    text = ''
    offset = 0
    nl = '\r\n' if '\r\n' in request.form['@0'] else '\n'
    for i in range(0, 12):
        if 'STACK MEMORY NODE' in request.form['@' + str(i)] or 'COMMUNICATION\nFAILURE' in request.form['@' + str(i)]:
            offset += 1
            continue
        text += '@' + str(i - offset) + nl + request.form['@' + str(i)]
        text += nl + nl
    response = make_response(text, 200)
    response.headers['Content-Disposition'] = 'attachment; filename=' + levelcode + '.0.txt'
    return response


@app.route('/<int:solution>', methods=['POST'])
def load_solution(solution):
    db = get_db()
    row = db.execute('SELECT * FROM solutions WHERE rowid=? AND master IS NULL', (solution,)).fetchone()
    if row is None:
        return ('Solution not found.', 404)
    textfields = dict()
    textfields['ports'] = row[14]
    textfields['levelcode'] = row[15]
    textfields['levelname'] = definitions.levels[textfields['levelcode']][13] if textfields['levelcode'] else ''
    for i in range(2, 14):
        textfields['@' + str(i - 2)] = row[i]
    return json.dumps(textfields)
    

@app.route('/<int:solution>/<int:fork>', methods=['POST'])
def load_fork(solution, fork):
    db = get_db()
    row = db.execute('SELECT * FROM solutions WHERE master=? AND forkno=?', (solution, fork)).fetchone()
    if row is None:
        return ('Solution not found.', 404)
    textfields = dict()
    textfields['ports'] = row[14]
    textfields['levelname'] = row[15]
    textfields['levelname'] = definitions.levels[textfields['levelcode']][13] if textfields['levelcode'] else ''
    for i in range(2, 14):
        textfields['@' + str(i - 2)] = row[i]
    return json.dumps(textfields)
