from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify

from app import db
from app.model.problem import Problem

import string
import math

mod = Blueprint('problems', __name__, url_prefix='/problem')

@mod.route('/<int:page>')
@mod.route('/')
def problems(page = 1):
 page = page -1
 return render_template("problems.html", items = Problem.query.offset(page*12).limit(12), page = page+1, maxPage = int(math.ceil(Problem.query.count()/12)) + 1)

@mod.route('/p/<string:problem>')
def problem(problem):
 return render_template("problem.html", problem = Problem.query.filter_by(identifier = problem).first())

@mod.route('/solutions.json')
def solutions():
 pass