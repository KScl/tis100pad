import os
import sys

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
'''app.config.from_object('config')'''

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

from app.views.home import mod as homeModule
app.register_blueprint(homeModule)

