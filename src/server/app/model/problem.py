from app import db
import json

class Problem(db.Model):
 EXEC = 0
 STCK = 1
 ERR = 2
 __tablename__ = "problem"
 id = db.Column(db.Integer, primary_key=True)
 identifier = db.Column(db.Text)
 name = db.Column(db.Text)
 userId = db.Column(db.Integer)
 script = db.Column(db.Text)
 entry1 = db.Column(db.Text)
 entry2 = db.Column(db.Text)
 entry3 = db.Column(db.Text)
 entry4 = db.Column(db.Text)
 output1 = db.Column(db.Text)
 output2 = db.Column(db.Text)
 output3 = db.Column(db.Text)
 output4 = db.Column(db.Text)
 descriptor = db.Column(db.Text)
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
 description = db.Column(db.Text)
 
 def __init__(self, a0 = None,a1 = None,a2 = None,a3 = None,a4 = None,a5 = None,a6 = None,a7 = None,a8 = None,a9 = None,a10 = None,a11 = None,entry1 = None,entry2 = None,entry3 = None,entry4 = None,output1 = None,output2 = None,output3  = None,output4 = None,userId = None,identifier = None,name = None,script = None,descriptor = None):
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
  self.entry1 = entry1
  self.entry2 = entry2
  self.entry3 = entry3
  self.entry4 = entry4
  self.output1 = output1
  self.output2 = output2
  self.output3 = output3
  self.output4 = output4
  self.descriptor =  descriptor
  self.name = name
  self.identifier = identifier
  self.script = script
  self.userId = userId


 def getEntries(self):
  return [self.entry1, self.entry2, self.entry3, self.entry4]

 def getOutput(self):
  return [self.output1, self.output2, self.output3, self.output4]

 def getRegisters(self):
  return [self.a0,self.a1,self.a2,self.a3,self.a4,self.a5,self.a6,self.a7,self.a8,self.a9,self.a10,self.a11]
 
 def __eq__(self, other):
  if isinstance(other, self.__class__):
   for x,y in zip(other.getRegisters(),self.getRegisters()):
    if x != y:
     return False

   for x,y in zip(other.getOutput(),self.getOutput()):
    if str(x) != str(y):
     return False

   for x,y in zip(other.getOutput(),self.getOutput()):
    if str(x) != str(y):
     return False
  else:
   return False
  return True
 
 def isValid(self):
  for register in self.getRegisters():
   if register != self.EXEC and register != self.STCK and register != self.ERR :
    return False
  return True
 
 def setRegister(self, index, value):
  if(index == 0):
   self.a0 = value
   return True
  elif(index == 1):
   self.a1 = value
   return True
  elif(index == 2):
   self.a2 = value
   return True
  elif(index == 3):
   self.a3 = value
   return True
  elif(index == 4):
   self.a4 = value
   return True
  elif(index == 5):
   self.a5 = value
   return True
  elif(index == 6):
   self.a6 = value
   return True
  elif(index == 7):
   self.a7 = value
   return True
  elif(index == 8):
   self.a8 = value
   return True
  elif(index == 9):
   self.a9 = value
   return True
  elif(index == 10):
   self.a10 = value
   return True
  elif(index == 11):
   self.a11 = value
   return True
  return False
 
 def setEntry(self,index, name,data):
  final = json.dumps({"name" : name,"data":data })
  if index == 0:
   self.entry1 = final
   return True
  elif index == 1:
   self.entry2 = final
   return True
  elif index == 2:
   self.entry3 = final
   return True
  elif index == 3:
   self.entry4 = final
   return True
  return False

 def setOutput(self,index, name,data):
  final = json.dumps({"name" : name,"data":data })
  if index == 0:
   self.output1 = final
   return True
  elif index == 1:
   self.output2 = final
   return True
  elif index == 2:
   self.output3 = final
   return True
  elif index == 3:
   self.output4 = final
   return True
  return False




 def getRegistersGrid(self):
   return [
   [self.a0,self.a1,self.a2,self.a3],
   [self.a4,self.a5,self.a6,self.a7],
   [self.a8,self.a9,self.a10,self.a11]]

 def __repr__(self):
  return '<problem %r>' % self.id