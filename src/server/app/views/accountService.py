from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify,json

from app import db
from app.model.problem import Problem
from app import app
import requests

from app.model.account import Account

from flask_kvsession import KVSessionExtension

import string
import math
import datetime

mod = Blueprint('account', __name__, url_prefix='/account')

@mod.route("/login.json", methods=['POST'])
def login():
 if(session.has_key("account.attempt")):
  if(session["account.attempt"] >= 3):
   if(session.has_key("account.delay") == False ):
    session["account.delay"] = datetime.datetime.now()
    return jsonify(result = False,output= [{'type':'danger', 'out' : "Try again in 00.05.00"}])
   else:
    time = ( datetime.datetime.now() - session["account.delay"] )
    if(time.total_seconds() > 60 * 5):
     session.pop("account.attempt")
     session.pop("account.delay")
    else:
     minutes, seconds = divmod((datetime.timedelta(minutes = 5)-time).total_seconds(), 60)
     return jsonify(result = False,output= [{'type':'danger', 'out' : "Try again in " + "00.{:02d}.{:02d}".format(int(minutes),int(seconds))}])
   

 name = request.get_json().get("name")
 password = request.get_json().get("password")
 account =Account.query.filter_by(name = name).first()
 if(account == None):
  return jsonify(result = False,output= [{'type':'danger', 'out' : "Invalid Login Attempt "+str(AddAttempt())+ " of 3"}])
 if account.checkPassword(password) == True:
  session["account.name"] = account.name
  session["account.id"] = account.id
  return jsonify(result = True)
 else:
  return jsonify(result = False,output= [{'type':'danger', 'out' : "Invalid Login Attempt "+str(AddAttempt())+ " of 3"}])
 return jsonify(result = False,output= [{'type':'danger', 'out' : "Invalid Login Attempt "+str(AddAttempt())+ " of 3"}])

def AddAttempt():
 if(session.has_key("account.attempt")):
  session["account.attempt"] = session["account.attempt"] + 1;
  return session["account.attempt"]
 session["account.attempt"] = 1
 return session["account.attempt"];


@mod.route("/create.json", methods=['POST'])
def createAccount():
 name = request.get_json().get("name")
 password = request.get_json().get("password")
 reEnterPassword = request.get_json().get("repeatPassword")
 captcha = request.get_json().get("captcha")
 secrete = app.config["RECAPTCHA_PRIVATE_TOKEN"]
 req = requests.get("https://www.google.com/recaptcha/api/siteverify",{
 	"secret":secrete,
    "response":captcha})
 results = json.loads(req.text)
 if Account.query.filter_by(name = request.get_json().get("name")).first() != None:
  return jsonify(result = False, output= [{'type':'danger', 'out' : "Username is Used"}])

 if results["success"] == True:
  account = Account(name,password)
  db.session.add(account)
  db.session.flush()
  session["account.name"] = account.name
  session["account.id"] = account.id
  db.session.commit()
  return jsonify(result = True)
 else:
  return jsonify(result = False, output= [{'type':'danger', 'out' :"Invalid Captcha"}])

@mod.route("/nameCheck.json",methods=['POST'])
def nameCheck():
 if Account.query.filter_by(name = request.get_json().get("name")).first() == None:
  return jsonify(result = True)
 else:
  return jsonify(result = False)


@mod.route("/verify.json",methods=['POST'])
def verify():
 if session.has_key("account.name"):
  return jsonify(result = True,name = session.get("account.name"), id = session.get("account.id"))
 return jsonify(result = False,name = "")


@mod.route("/logout.json",methods=['POST'])
def logout():
 session.pop("account.name")
 session.pop("account.id")
 return jsonify(result = True)