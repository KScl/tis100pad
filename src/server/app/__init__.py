import os
import sys
import redis

from flask import Flask, render_template,redirect
from flask.ext.sqlalchemy import SQLAlchemy

from flask_kvsession import KVSessionExtension
from simplekv.memory.redisstore import RedisStore

store = RedisStore(redis.StrictRedis())

app = Flask(__name__)
KVSessionExtension(store, app)

app.config.from_object('config')

db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

@app.context_processor
def inject_recaptcha():
 return dict(public_token = app.config["RECAPTCHA_PUBLIC_TOKEN"])

@app.route('/')
def index():
 return redirect("/pad", code=302)

@app.context_processor
def inject_user():
    return dict(googleTrackingCode=app.config["GOOGLE_ANALYTICS_CODE"])

from app.views.solutionSubmitService import mod as solutionSubmitModule
app.register_blueprint(solutionSubmitModule)

from app.views.problemSubmitService import mod as problemSubmitModule
app.register_blueprint(problemSubmitModule)


from app.views.problemService import mod as problemModule
app.register_blueprint(problemModule)

from app.views.accountService import mod as accountModule
app.register_blueprint(accountModule)

from app.views.userService import mod as userModule
app.register_blueprint(userModule)
