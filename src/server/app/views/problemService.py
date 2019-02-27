from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify

from app import db
from app.model.problem import Problem
from app.model.solution import Solution
from app.model.account import Account

import string
import math

mod = Blueprint('problems', __name__, url_prefix='/problem')

@mod.route('/')
def problems():
 return render_template("problems.html", 
  total = Problem.query.filter(Problem.userId != None).count())

@mod.route('/p/download/<string:problem>')
def download_problem(problem):
 problem = Problem.query.filter(Problem.identifier == problem)
 return problem.first().script

@mod.route('/p/<string:problem>')
def problem(problem):
 problem = Problem.query.filter_by(identifier = problem).first()
 return render_template("problem.html", 
  id = problem.id,
  IsUserProblem = (problem.script != None),
  name = problem.name, 
  identifier = problem.identifier,
  hasCode = problem.script != None)

@mod.route('/problemPage.json',methods=['POST'])
def problemPage():
 page = int(request.get_json().get("page"))-1
 problem_type = request.get_json().get("type")
 problem_query = 0
 if(problem_type == "USER_CREATED"):
  problem_query = Problem.query.filter(Problem.userId != -1 , Problem.identifier != None)
 else:
  problem_query = Problem.query.filter(Problem.userId == -1, Problem.identifier != None)
 results = []
 for problem in problem_query.offset(page*12).limit(12):
  results.append({"name" : problem.name, "description" : problem.description, "identifier" : problem.identifier})
 return jsonify(result = results, count = problem_query.count())

@mod.route('/solutionPage.json',methods=['POST'])
def solutionPage():
 ordering = request.get_json().get("ordering")
 page =  int(request.get_json().get("page")) -1
 problem = Problem.query.filter_by(id = request.get_json().get("problemId")).first()
 if ordering == "CYL":
  return jsonify({"results" :Solution.simpleJsonify(Solution.query.filter_by(problemId = problem.id).order_by(db.desc(Solution.cycles)).offset(page*12).limit(12))})
 elif ordering == "NOD":
  return jsonify({"results" :Solution.simpleJsonify(Solution.query.filter_by(problemId = problem.id).order_by(db.desc(Solution.nodeCount)).offset(page*12).limit(12))})
 elif ordering == "INS":
  return jsonify({"results" :Solution.simpleJsonify(Solution.query.filter_by(problemId = problem.id).order_by(db.desc(Solution.instructionCount)).offset(page*12).limit(12))})
