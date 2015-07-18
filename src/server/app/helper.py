from flask.ext.sqlalchemy import SQLAlchemy
from flask import  g

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = SQLAlchemy(application)
    return db