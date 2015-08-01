from app import db

import hashlib

class Account(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 name = db.Column(db.String(80))
 password = db.Column(db.String(120))
 
 def __init__(self,name,password):
  self.name = name
  hash = hashlib.sha256()
  hash.update(password)
  hash.update(app.config["PASSWORD_HASH"])
  self.password = hash.digest().hexdigest()

 def checkPassword(password):
  hash = hashlib.sha256()
  hash.update(password)
  hash.update(app.config["PASSWORD_HASH"])
  password = hash.digest().hexdigest()
  if(password == self.password):
   return True
  return False
