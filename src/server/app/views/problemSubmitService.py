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