from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify,json

from app import db
from app.model.problem import Problem
from app import app
import requests

import string
import math

mod = Blueprint('account', __name__, url_prefix='/account')

@mod.route("/login.json")
def login():
 return ""

@mod.route("/create.json", methods=['POST'])
def createAccount():
 name = request.get_json().get("name")
 password = request.get_json().get("password")
 reEnterPassword = request.get_json().get("repassword")
 captcha = request.get_json().get("captcha")

 req = requests.get("https://www.google.com/recaptcha/api/siteverify",{
 	"secret": app.config["RECAPTCHA_PRIVATE_TOKEN"],
    "response":captcha})
 results = json.loads(req.text)
 print results
 if results.success == True:
  return req.text
 else:
  return jsonify(result = "Failed")