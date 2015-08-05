from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify

from app import db
from app.model.problem import Problem
from app.model.solution import Solution

import string
import math

mod = Blueprint('problems', __name__, url_prefix='/problem')

@mod.route('/<int:page>')
@mod.route('/')
def problems(page = 1):
 page = page -1
 return render_template("problems.html", 
  total = Problem.query.filter(Problem.userId != None).count())

 '''return render_template("problems.html", items = Problem.query.filter(Problem.userId != None).offset(page*12).limit(12), page = page+1, maxPage = int(math.ceil(Problem.query.filter(Problem.userId != None).count()/12)) + 1)'''

@mod.route('/p/<string:problem>')
def problem(problem):
 return render_template("problem.html", problem = Problem.query.filter_by(identifier = problem).first())

def solutionsJsonify(data):
 output = []
 for item in data:
  output.append({'cycles' :item.cycles , 'nodeCount' : item.nodeCount ,'instructionCount': item.instructionCount, 'id' : item.id});
 return jsonify({"results" : output})


@mod.route('/solutions.json', methods=['POST'])
def solutions():
 ordering = request.get_json().get("ordering")
 page = request.get_json().get("page")
 problem = Problem.query.filter_by(id = request.get_json().get("problemId")).first()
 if ordering == "CYL":
  return solutionsJsonify(Solution.query.filter_by(problemId = problem.id).order_by(db.desc(Solution.cycles)).offset(page*12).limit(12))
 elif ordering == "NOD":
  return solutionsJsonify(Solution.query.filter_by(problemId = problem.id).order_by(db.desc(Solution.nodeCount)).offset(page*12).limit(12))
 elif ordering == "INS":
  return solutionsJsonify(Solution.query.filter_by(problemId = problem.id).order_by(db.desc(Solution.instructionCount)).offset(page*12).limit(12))

@mod.route('/page.json',methods=['POST'])
def page():
 page = request.get_json().get("page")-1
 results = []
 for problem in Problem.query.filter(Problem.userId != None).offset(page*12).limit(12):
  results.append({"name" : problem.name, "description" : problem.description, "identifier" : problem.identifier})
 return jsonify(result = results)