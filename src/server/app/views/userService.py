from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify,json

from app import db
from app import app
import requests

from app.model.problem import Problem
from app.model.solution import Solution
from app.model.account import Account

import string
import math

mod = Blueprint('user', __name__, url_prefix='/user')

@mod.route('/<string:user>')
@mod.route('/')
def root(user = ''):
 user = Account.query.filter_by(name = user).first()
 owner = "false"
 if session.has_key("account.name"):
  if session["account.name"] == user.name:
   owner = "true"
 return render_template("user.html",owner = owner,user = user.name ,solutions_total = Solution.query.filter_by(userId = user.id).count())

@mod.route('/changePassword.json',methods=['POST'])
def changePassword():
 oldPassword = request.get_json().get("oldPassword")
 newPassword = request.get_json().get("newPassword")

 if session.has_key("account.id") == False:
  return jsonify(result = False, output= [{'type':'danger', 'out' : "Account Session Expired"}])

 account = Account.query.filter_by(id = session["account.id"]).first()
 if(account.checkPassword(oldPassword) == True):
  account.changePassword(newPassword)
  db.session.commit()
  return jsonify(result = True,output= [{'type':'success', 'out' : "Password Updated"}])
 else:
  return jsonify(result = True,output= [{'type':'danger', 'out' : "Invalid old password"}])
 return jsonify(result = False, output= [{'type':'danger', 'out' : "Try Again"}])

@mod.route('/problemsPage.json',methods=['POST'])
def problemPage():
 page = int(request.get_json().get("page"))-1
 results = []
 user = Account.query.filter_by(name = request.get_json().get("user")).first()
 for problem in Problem.query.filter(Problem.identifier != None,Problem.userId == user.id).offset(page*12).limit(12):
  results.append({"name" : problem.name, "description" : problem.description, "identifier" : problem.identifier})
 return jsonify(results = results, total = Problem.query.filter(Problem.identifier != None,Problem.userId == user.id).count())

@mod.route('/solution_list.json',methods=['POST'])
def solution_list():
 user = Account.query.filter_by(name = request.get_json().get("user")).first()
 problem_id = request.get_json().get("problem_id")
 ordering = request.get_json().get("ordering")
 solution_query = None
 if(problem_id == -1):
  if ordering == "CYL":
   solution_query = Solution.query.filter(Solution.userId == user.id, Problem.identifier == None).join(Problem, Problem.id == Solution.problemId).order_by(db.desc(Solution.cycles))
  elif ordering == "NOD":
   solution_query = Solution.query.filter(Solution.userId == user.id, Problem.identifier == None).join(Problem, Problem.id == Solution.problemId).order_by(db.desc(Solution.nodeCount))
  elif ordering == "INS":
   solution_query = Solution.query.filter(Solution.userId == user.id, Problem.identifier == None).join(Problem, Problem.id == Solution.problemId).order_by(db.desc(Solution.instructionCount))
 else:
  if ordering == "CYL":
   solution_query = Solution.query.filter(Solution.userId == user.id ,  Solution.problemId == problem_id).order_by(db.desc(Solution.cycles))
  elif ordering == "NOD":
   solution_query = Solution.query.filter(Solution.userId == user.id ,  Solution.problemId == problem_id).order_by(db.desc(Solution.nodeCount))
  elif ordering == "INS":
   solution_query = Solution.query.filter(Solution.userId == user.id ,  Solution.problemId == problem_id).order_by(db.desc(Solution.instructionCount))
 return jsonify({"results" : Solution.simpleJsonify(solution_query)})



@mod.route('/solutionPage.json',methods=['POST'])
def solutionPage():
 ordering = request.get_json().get("ordering")
 page =  int(request.get_json().get("page")) -1
 user = Account.query.filter_by(name = request.get_json().get("user")).first()
 problem_query = Problem.query.join(Solution,Problem.id == Solution.problemId).filter(Solution.userId == user.id, Problem.identifier != None)
 # .filter_by(userId = user.id)
 results = []
 if(Problem.query.join(Solution,Problem.id == Solution.problemId).filter(Solution.userId == user.id, Problem.identifier == None).count() > 0):
  results.append({"name" : "NILL","id" : -1, "description" : "--", "identifier" : "--"})
 for item in problem_query:
  results.append({"name" : item.name,"id" : item.id, "description" : item.description, "identifier" : item.identifier})
 return jsonify(results = results)
 # if ordering == "CYL":
 #  return jsonify({"results" : Solution.simpleJsonify(solution_query.order_by(db.desc(Solution.cycles)).offset(page*12).limit(12)), "total" : solution_query.count()})
 # elif ordering == "NOD":
 #  return jsonify({"results" : Solution.simpleJsonify(solution_query.order_by(db.desc(Solution.nodeCount)).offset(page*12).limit(12)), "total" : solution_query.count()})
 # elif ordering == "INS":
 #  return jsonify({"results" : Solution.simpleJsonify(solution_query.order_by(db.desc(Solution.instructionCount)).offset(page*12).limit(12)), "total" : solution_query.count()})
