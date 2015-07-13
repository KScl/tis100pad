import os
import sys

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.run(debug=app.config["DEBUG"])

db = SQLAlchemy(app)
