from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify,json

from app import db
from app.model.problem import Problem
from app import app
import requests

from app.model.account import Account

import string
import math

mod = Blueprint('user', __name__, url_prefix='/user')

@mod.route('/')
def root():
 return render_template("user.html")