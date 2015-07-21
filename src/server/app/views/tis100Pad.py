from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify

from app import db
from app.model.solution import Solution
from app.model.problem import Problem

import string

mod = Blueprint('pad', __name__, url_prefix='/pad')

@mod.route('.html')
def root():
 return render_template("PadView.html")

@mod.route('/solution/<int:solution>', methods=['POST','GET'])
def getSolution(solution):
 solution = Solution.query.filter_by(id = solution).first();
 problem = Problem.query.filter_by(id = solution.problemId).first();
 return jsonify({
  'grid': solution.getRegistersGrid(), 
  'states' : problem.getRegistersGrid(), 
  "problemId" : problem.id , 
  "inputs" : problem.getEntries(),
  "outputs" : problem.getOutput(),
  "name" : problem.name, 
  "identifier" : problem.identifier})

@mod.route('/save.json', methods=['POST'])
def save():
 nodes = request.get_json().get("nodes")
 problem = Problem(
  nodes[0][0].get("state"),nodes[0][1].get("state"),nodes[0][2].get("state"),nodes[0][3].get("state"),
  nodes[1][0].get("state"),nodes[1][1].get("state"),nodes[1][2].get("state"),nodes[1][3].get("state"),
  nodes[2][0].get("state"),nodes[2][1].get("state"),nodes[2][2].get("state"),nodes[2][3].get("state"),0,0,0,0,0,0,0,0)
 matching = True

 for item in problem.getRegisters():
  if not (item == Problem.EXEC or item == Problem.ERR or item == Problem.STCK):
   return render_template('404.html'), 403

 if request.get_json().get("problemId") != -1 :
  problemById = Problem.query.filter_by(id = request.get_json().get("problemId")).first()
  for i in range(len(problemById.getRegisters())):
   if problem.getRegisters()[i] != problemById.getRegisters()[i]:
    problem = problemById
    break
 
 db.session.add(problem)
 db.session.flush()
 solution = Solution( 
  nodes[0][0].get("text"),nodes[0][1].get("text"),nodes[0][2].get("text"),nodes[0][3].get("text"),
  nodes[1][0].get("text"),nodes[1][1].get("text"),nodes[1][2].get("text"),nodes[1][3].get("text"),
  nodes[2][0].get("text"),nodes[2][1].get("text"),nodes[2][2].get("text"),nodes[2][3].get("text"),problem.id)
 db.session.add(solution)
 db.session.flush()
 db.session.commit()
 return jsonify(id= solution.id)

@mod.route('/problem.json', methods=['POST'])
def problem():
 problem = None
 if request.get_json().get('identifier'):
  problem = Problem.query.filter_by(identifier =request.get_json().get('identifier')).first()

 outputs = ["","","","","","","","","","","",""]
 register = problem.getRegisters()
 lines = request.get_json().get('file').split("@")[1:]

 lnindex = 0
 for index,reg in enumerate(register):
  if reg == Problem.EXEC:
   out =  lines[lnindex]
   outputs[index] = out[out.index("\n"):].strip()
   lnindex += 1

 db.session.flush()
 solution = Solution(
  outputs[0],
  outputs[1],
  outputs[2],
  outputs[3],
  outputs[4],
  outputs[5],
  outputs[6],
  outputs[7],
  outputs[8],
  outputs[9],
  outputs[10],
  outputs[11],
  problem.id)
 db.session.add(solution)
 db.session.commit()
 return jsonify(id= solution.id)
