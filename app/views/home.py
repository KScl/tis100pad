from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify

from app import db
from app.model.solution import Solution

mod = Blueprint('pad', __name__, url_prefix='/')

@mod.route('')
def root():
	return render_template("index.html")

@mod.route('<int:solution>')
def getSolution(solution):
	return render_template("index.html",solution = Solution.query.filter_by(id = solution).first())

@mod.route('save')
def save():
	return jsonify(saved=True)
