import os
import sys

from flask import Flask, render_template,redirect
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

@app.route('/')
def index():
 return redirect("/pad", code=302)

from app.views.padService import mod as padModule
app.register_blueprint(padModule)

from app.views.problemService import mod as problemModule
app.register_blueprint(problemModule)

from app.views.accountService import mod as accountModule
app.register_blueprint(accountModule)
