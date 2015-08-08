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

@mod.route('/p/<string:problem>')
def problem(problem):
 problem = Problem.query.filter_by(identifier = problem).first()
 return render_template("problem.html", 
  total = Solution.query.filter_by(problemId = problem.id).count(), 
  id = problem.id,
  name = problem.name, 
  identifier = problem.identifier)

def solutionsJsonify(data):
 output = []
 for item in data:
  account = Account.query.filter_by(id = item.userId).first()
  name = None
  if(account != None):
   name = account.name
  output.append({'cycles' :item.cycles , 'nodeCount' : item.nodeCount ,'instructionCount': item.instructionCount, 'id' : item.id, 'name' : name});
 return jsonify({"results" : output})


@mod.route('/problemPage.json',methods=['POST'])
def problemPage():
 page = int(request.get_json().get("page"))-1
 results = []
 for problem in Problem.query.filter(Problem.userId != None).offset(page*12).limit(12):
  results.append({"name" : problem.name, "description" : problem.description, "identifier" : problem.identifier})
 return jsonify(result = results)

@mod.route('/solutionPage.json',methods=['POST'])
def solutionPage():
 ordering = request.get_json().get("ordering")
 page =  int(request.get_json().get("page")) -1
 problem = Problem.query.filter_by(id = request.get_json().get("problemId")).first()
 if ordering == "CYL":
  return solutionsJsonify(Solution.query.filter_by(problemId = problem.id).order_by(db.desc(Solution.cycles)).offset(page*12).limit(12))
 elif ordering == "NOD":
  return solutionsJsonify(Solution.query.filter_by(problemId = problem.id).order_by(db.desc(Solution.nodeCount)).offset(page*12).limit(12))
 elif ordering == "INS":
  return solutionsJsonify(Solution.query.filter_by(problemId = problem.id).order_by(db.desc(Solution.instructionCount)).offset(page*12).limit(12))
