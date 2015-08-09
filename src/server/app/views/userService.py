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


@mod.route('/solutionPage.json',methods=['POST'])
def solutionPage():
 ordering = request.get_json().get("ordering")
 page =  int(request.get_json().get("page")) -1
 user = Account.query.filter_by(name = request.get_json().get("user")).first()
 if ordering == "CYL":
  return Solution.simpleJsonify(Solution.query.filter_by(userId = user.id).order_by(db.desc(Solution.cycles)).offset(page*12).limit(12))
 elif ordering == "NOD":
  return Solution.simpleJsonify(Solution.query.filter_by(userId = user.id).order_by(db.desc(Solution.nodeCount)).offset(page*12).limit(12))
 elif ordering == "INS":
  return Solution.simpleJsonify(Solution.query.filter_by(userId = user.id).order_by(db.desc(Solution.instructionCount)).offset(page*12).limit(12))
