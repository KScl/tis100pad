from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from app import db
from app.model.solution import Solution

mod = Blueprint('pad', __name__, url_prefix='/')

@mod.route('/')
def root():
	return render_template("index.html")