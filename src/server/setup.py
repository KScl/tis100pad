import commands

from flask import *
from app import *
app.config.from_object('config')

db.create_all()

from app import problems

