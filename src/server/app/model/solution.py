from app import db
from app.model.problem import Problem
from app.model.account import Account
import datetime

from flask import jsonify

import re

class Solution(db.Model):
 __tablename__ = "solution"
 id = db.Column(db.Integer, primary_key=True)
 problemId = db.Column(db.Integer)
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
 date = db.Column(db.Date)
 a11 = db.Column(db.Text)
 cycles = db.Column(db.Integer)
 nodeCount = db.Column(db.Integer)
 instructionCount = db.Column(db.Integer)
 userId = db.Column(db.Integer)

 def countInstructions(self,input):
  intstructions = 0
  lines = re.split("\r\n|\r|\n",input)
  for line in lines:
   if(not (line.strip() == "" or line.strip()[:1] == "#")):
    intstructions+=1
  return intstructions

 def countNodes(self,input):
  return int(input.strip() != "")

 def __init__(self, a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,problemId,userId = None):
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
  self.problemId = problemId
  self.userId = userId
  self.date = datetime.datetime.now()

  self.cycles = -1
  self.nodeCount = 0
  self.instructionCount = 0
  
  for register in self.getRegisters():
   self.nodeCount += self.countNodes(register)
   self.instructionCount += self.countInstructions(register)

 def getRegisters(self):
  return [self.a0,self.a1,self.a2,self.a3,self.a4,self.a5,self.a6,self.a7,self.a8,self.a9,self.a10,self.a11]

 def getRegistersGrid(self):
  return [
  [self.a0,self.a1,self.a2,self.a3],
  [self.a4,self.a5,self.a6,self.a7],
  [self.a8,self.a9,self.a10,self.a11]]

 def getProblem(self):
  return Problem.query.filter_by(id = self.problemId).first();

 def getFile(self):
  levelcode = self.levelcode if self.levelcode else 'level'
  text = ''
  offset = 0
  for i in range(0, 12):
   text += '@' + str(i - offset) + '\n' + self.getRegisters()[i].upper()
   text += '\n\n'
  return text

 def isEmpty(self):
  if self.a0 == "" and self.a1 == "" and self.a2 == "" and self.a3 == "" and self.a4 == "" and self.a5 == "" and self.a6 == "" and self.a7 == "" and self.a8 == "" and self.a9 == "" and self.a10 == "" and self.a11 == "" :
   return True
  return False
 
 def equal(self,solution):
  if solution.a0 == self.a0 and solution.a1 == self.a1 and solution.a2 == self.a2 and solution.a3 == self.a3 and solution.a4 == self.a4 and solution.a5 == self.a5 and solution.a6 == self.a6 and solution.a7 == self.a7 and solution.a8 == self.a8 and solution.a9 == self.a9 and solution.a10 == self.a10 and solution.a11 == self.a11 :
   return True
  return False
 
 @staticmethod
 def simpleJsonify(solutions):
  output = []
  for item in solutions:
   account = Account.query.filter_by(id = item.userId).first()
   name = None
   if(account != None):
    name = account.name
   output.append({'cycles' :item.cycles , 'nodeCount' : item.nodeCount ,'instructionCount': item.instructionCount, 'id' : item.id, 'name' : name});
  return output



 def __repr__(self):
  return '<solution %r>' % self.id