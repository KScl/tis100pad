from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify

from app import db
from app.model.solution import Solution
from app.model.problem import Problem

import string

mod = Blueprint('problems', __name__, url_prefix='/problems')

@mod.route('/<int:solution>')
@mod.route('/')
def root(solution = -1):
 return render_template("problemList.html",solutionId = solution)