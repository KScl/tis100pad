from app import db

class Solution(db.Model):

	__tablename__ = "solution"
	id = db.Column(db.Integer, primary_key=True)
	a0 = db.Column(db.Text)
	a1 = db.Column(db.Text)
	a2 = db.Column(db.Text)
	a3 = db.Column(db.Text)
	a4 = db.Column(db.Text)
	a5 = db.Column(db.Text)
	a6 = db.Column(db.Text)
	a7 = db.Column(db.Text)
	a8 = db.Column(db.Text)
	a9 = db.Column(db.Text)
	a10 = db.Column(db.Text)
	a11 = db.Column(db.Text)
	ports = db.Column(db.Text)
	levelcode = db.Column(db.Text)

	def __init__(self, a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,ports,levelcode):
		self.a0 = a0
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		self.a4 = a4
		self.a5 = a5
		self.a6 = a6
		self.a7 = a7
		self.a8 = a8
		self.a9 = a9
		self.a10 = a10
		self.a11 = a11
		self.ports = ports
		self.levelcode = levelcode

	def getRegisters(self):
		return [self.a0,self.a1,self.a2,self.a3,self.a4,self.a5,self.a6,self.a7,self.a8,self.a9,self.a10,self.a11]

	def getFile(self):
		levelcode = self.levelcode if self.levelcode else 'level'
		text = ''
		offset = 0
		for i in range(0, 12):
			if '@' + str(i) not in request.form:
				offset += 1
				continue
			text += '@' + str(i - offset) + '\n' + getRegisters()[i].upper()
			text += '\n\n'
		return text

	def __repr__(self):
		return '<User %r>' % self.username