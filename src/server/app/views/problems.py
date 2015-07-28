from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify

from app import db
from app.model.problem import Problem

import string
import math

mod = Blueprint('problems', __name__, url_prefix='/problems')

@mod.route('/<int:page>')
@mod.route('/')
def root(page = 1):
 page = page -1
 return render_template("problems.html", items = Problem.query.offset(page*12).limit(12), page = page+1, maxPage = int(math.ceil(Problem.query.count()/12)) + 1)