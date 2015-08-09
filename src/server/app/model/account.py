from app import db

import hashlib
from app import app

class Account(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 name = db.Column(db.String(80))
 password = db.Column(db.String(120))
 
 def __init__(self,name,password):
  self.name = name
  hash = hashlib.sha256()
  hash.update(password)
  hash.update(app.config["PASSWORD_HASH"])
  self.password = hash.hexdigest()

 def checkPassword(self,password):
  hash = hashlib.sha256()
  hash.update(password)
  hash.update(app.config["PASSWORD_HASH"])
  password = hash.hexdigest()
  if(password == self.password):
   return True
  return False

 def changePassword(self,password):
  hash = hashlib.sha256()
  hash.update(password)
  hash.update(app.config["PASSWORD_HASH"])
  self.password = hash.hexdigest() 
  return self.password 

 @staticmethod
 def HashPassword(password):
  hash = hashlib.sha256()
  hash.update(password)
  hash.update(app.config["PASSWORD_HASH"])
  return hash.hexdigest()
