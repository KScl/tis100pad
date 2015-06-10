# -*- coding: utf-8 -*-

from flask import Flask, request, g, json
from logging import FileHandler
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
    row = (master, forkno,
           request.form['@0'], request.form['@1'], request.form['@2'], request.form['@3'], 
           request.form['@4'], request.form['@5'], request.form['@6'], request.form['@7'], 
           request.form['@8'], request.form['@9'], request.form['@10'], request.form['@11'])
    if currentfork:
        if row[2:14] == db.execute('SELECT * FROM solutions WHERE master=? AND forkno=?', (master, currentfork)).fetchone()[2:14]:
            return ('No changes.', 202)
    elif master:
        if row[2:14] == db.execute('SELECT * FROM solutions WHERE rowid=?',(master,)).fetchone()[2:14]:
            return ('No changes.', 202)           
    newrow = db.execute('INSERT INTO solutions VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row).lastrowid
    db.commit()
    return str(newrow if not forkno else master) + '/' + str(forkno if forkno else 0)


@app.route('/upload', methods=['POST'])
def upload_save():
    file = request.files['file']
    levelname = file.filename.split('.')[0]
    if levelname not in definitions.levels:
        return ('Invalid file.', 400)
    entries = file.read().split('@')
    textfields = dict()
    incrementer = 0
    for entry in entries:
        if entry == '':
            continue
        nl = entry.find('\n')
        entryno = str(int(entry[0:nl]) + incrementer)
        if definitions.levels[levelname][int(entryno)] == 1:
            textfields['@' + entryno] = '\n\n\n\n\n█████████████████\n\nSTACK MEMORY NODE\n\n█████████████████'
            textfields['@' + str(int(entryno) + 1)] = entry[nl + 1:]
            incrementer += 1
        elif definitions.levels[levelname][int(entryno)] == 2:
            textfields['@' + entryno] = '\n\n\n\n██████████████\n\nCOMMUNICATION\nFAILURE\n\n██████████████'
            textfields['@' + str(int(entryno) + 1)] = entry[nl + 1:]
            incrementer += 1
        else:
            textfields['@' + entryno] = entry[nl + 1:]
    return json.dumps(textfields)


@app.route('/<int:solution>', methods=['POST'])
def load_solution(solution):
    db = get_db()
    row = db.execute('SELECT * FROM solutions WHERE rowid=? AND master=?', (solution, None)).fetchone()
    if row is None:
        return ('Solution not found.', 404)
    textfields = dict()
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
    for i in range(2, 14):
        textfields['@' + str(i - 2)] = row[i]
    return json.dumps(textfields)