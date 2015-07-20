import os
import sys

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

@app.route('/')
def index():
 return render_template("index.html")

from app.views.tis100Pad import mod as tis100PadModule
app.register_blueprint(tis100PadModule)
