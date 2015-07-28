from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify

from app import db
from app.model.problem import Problem

import string

mod = Blueprint('problems', __name__, url_prefix='/problems')

@mod.route('/<int:page>')
@mod.route('/')
def root(page = 0):
 return render_template("problems.html", items = Problem.query.offset(page*10).limit(10))