from app import db

class Problem(db.Model):
 EXEC = 0
 STCK = 1
 ERR = 2
 __tablename__ = "problem"
 id = db.Column(db.Integer, primary_key=True)
 identifier = db.Column(db.Text)
 name = db.Column(db.Text)
 script = db.Column(db.Text)
 entrt1 = db.Column(db.Text)
 entrt2 = db.Column(db.Text)
 entrt3 = db.Column(db.Text)
 entrt4 = db.Column(db.Text)
 output1 = db.Column(db.Text)
 output2 = db.Column(db.Text)
 output3 = db.Column(db.Text)
 output4 = db.Column(db.Text)
 a0 = db.Column(db.Integer)
 a1 = db.Column(db.Integer)
 a2 = db.Column(db.Integer)
 a3 = db.Column(db.Integer)
 a4 = db.Column(db.Integer)
 a5 = db.Column(db.Integer)
 a6 = db.Column(db.Integer)
 a7 = db.Column(db.Integer)
 a8 = db.Column(db.Integer)
 a9 = db.Column(db.Integer)
 a10 = db.Column(db.Integer)
 a11 = db.Column(db.Integer)

 def __init__(self, a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,entrt1,entrt2,entrt3,entrt4,output1,output2,output3,output4,identifier = None,name = None,script = None):
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
  self.entrt1 = entrt1
  self.entrt2 = entrt2
  self.entrt3 = entrt3
  self.entrt4 = entrt4
  self.output1 = output1
  self.output2 = output2
  self.output3 = output3
  self.output4 = output4
  self.name = name
  self.identifier = identifier
  self.script = script

 def getEntries(self):
  return [self.entrt1, self.entrt2, self.entrt3, self.entrt4]

 def getOutput(self):
  return [self.output1, self.output2, self.output3, self.output4]

 def getRegisters(self):
  return [self.a0,self.a1,self.a2,self.a3,self.a4,self.a5,self.a6,self.a7,self.a8,self.a9,self.a10,self.a11]

 def getRegistersGrid(self):
   return [
   [self.a0,self.a1,self.a2,self.a3],
   [self.a4,self.a5,self.a6,self.a7],
   [self.a8,self.a9,self.a10,self.a11]]

 def __repr__(self):
  return '<problem %r>' % self.id