from app import db

class Solution(db.Model):

	__tablename__ = "solution"
	id = db.Column(db.Integer, primary_key=True)
	master = db.Column(db.Integer)
	forkno = db.Column(db.Integer)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username