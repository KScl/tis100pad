from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify,json

from app import db
from app.model.problem import Problem
from app import app
import requests

from app.model.account import Account

import string
import math

mod = Blueprint('account', __name__, url_prefix='/account')

@mod.route("/login.json", methods=['POST'])
def login():
 name = request.get_json().get("name")
 password = request.get_json().get("password")
 account =Account.query.filter_by(name = name).first()
 if(account == None):
  return jsonify(result = False)
 if account.checkPassword(password) == True:
  session["account.name"] = account.name
  session["account.id"] = account.id
  return jsonify(result = True)
 else:
  return jsonify(result = False)

@mod.route("/create.json", methods=['POST'])
def createAccount():
 name = request.get_json().get("name")
 password = request.get_json().get("password")
 reEnterPassword = request.get_json().get("repeatPassword")
 captcha = request.get_json().get("captcha")
 secrete = app.config["RECAPTCHA_PRIVATE_TOKEN"]
 print captcha
 req = requests.get("https://www.google.com/recaptcha/api/siteverify",{
 	"secret":secrete,
    "response":captcha})
 results = json.loads(req.text)
 if results["success"] == True:
  account = Account(name,password)
  db.session.add(account)
  db.session.flush()
  db.session.commit();
  return jsonify(result = True)
 else:
  return jsonify(result = False, err = results['error-codes'])

@mod.route("/nameCheck.json",methods=['POST'])
def nameCheck():
 if Account.query.filter_by(name = request.get_json().get("name")).first() == None:
  return jsonify(result = True)
 else:
  return jsonify(result = False)


@mod.route("/verify.json",methods=['POST'])
def verify():
 if session.has_key("account.name"):
  return jsonify(result = True,name = session.get("account.name"))
 return jsonify(result = False,name = "")


@mod.route("/logout.json",methods=['POST'])
def logout():
 session.pop("account.name")
 session.pop("account.id")
 return jsonify(result = True)