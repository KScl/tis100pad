from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify, redirect
from app import db
from app.model.solution import Solution
from app.model.problem import Problem
from app.model.account import Account

import string

mod = Blueprint('problemPad', __name__, url_prefix='/problemPad')

@mod.route('/')
def root():
 return render_template("problemPad.html")

@mod.route('/IdentifierCheck.json',methods=['POST'])
def IdentityCheck():
 if Problem.query.filter_by(identifier = request.get_json().get("identifier")).first() == None:
  return jsonify(result = True)
 else:
  return jsonify(result = False)

@mod.route('/submit.json',methods=['POST'])
def submit():
 if Problem.query.filter_by(identifier = request.get_json().get("identifier")).first() != None:
  return jsonify(result = True)
 return jsonify(result = False)