from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify

from app import db
from app.model.problem import Problem

import string
import math

mod = Blueprint('account', __name__, url_prefix='/account')

@mod.route("/login.json")
def login():
 return "";

@mod.route("/create.json")
def createAccount():
 name = request.get_json().get("name")
 password = request.get_json().get("password")
 reEnterPassword = request.get_json().get("repassword")
 captcha = request.get_json().get("captcha")