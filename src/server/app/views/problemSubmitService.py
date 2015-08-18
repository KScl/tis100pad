from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify, redirect
from app import db
from app.model.solution import Solution
from app.model.problem import Problem
from app.model.account import Account

import json
import lupa
import string

mod = Blueprint('problemPad', __name__, url_prefix='/problemPad')

@mod.route('/')
def root():
 return render_template("problemPad.html")

@mod.route('/IdentifierCheck.json',methods=['POST'])
def IdentityCheck():
 if Problem.query.filter_by(identifier = request.get_json().get("identifier")).first() == None:
  return jsonify(result = True)
 else:
  return jsonify(result = False)

@mod.route('/submit.json',methods=['POST'])
def submit():
 if Problem.query.filter_by(identifier = request.get_json().get("identifier")).first() == None:
  lua = lupa.LuaRuntime()
  run = lua.eval('''
   function(c)
    local BASE_ENV = {}
([[
math.abs   math.acos math.asin  math.atan math.atan2 math.ceil
math.cos   math.cosh math.deg   math.exp  math.fmod  math.floor
math.frexp math.huge math.ldexp math.log  math.log10 math.max
math.min   math.modf math.pi    math.pow  math.rad   math.random
math.sin   math.sinh math.sqrt  math.tan  math.tanh
string.byte string.char  string.find  string.format string.gmatch
string.gsub string.len   string.lower string.match  string.reverse
]]):gsub('%S+', function(id)
  local module, method = id:match('([^%.]+)%.([^%.]+)')
  if module then
    BASE_ENV[module]         = BASE_ENV[module] or {}
    BASE_ENV[module][method] = _G[module][method]
  else
    BASE_ENV[id] = _G[id]
  end
end)

    local untrusted_function, message = load(c, nil, 't', BASE_ENV)
    if not untrusted_function then return nil, message end
    return pcall(untrusted_function)
   end
  ''')
  output = run('''
   STREAM_INPUT = 0
   STREAM_OUTPUT = 1

   TILE_COMPUTE = 0
   TILE_MEMORY = 1
   TILE_DAMAGED = 2
   ''' +
   request.get_json().get("code") + '''
   return get_name(), get_description(), get_streams(), get_layout()
   ''')

  if output[0] != None:
   problem = Problem()
   problem.name = output[1]
   descriptors = []
   for x in output[2]:
    descriptors.append(output[2][x])
   problem.descriptor = json.dumps(descriptors)

   for x in output[3]:
    data = []
    for y in output[3][x][4]:
     if output[3][x][4][y] > 999 or output[3][x][4][y] < -999:
      return jsonify(result = False, err = [{'type':'danger', 'out' : "input or ouput are out of bound [-999,999] "}])
     data.append(output[3][x][4][y])
    if output[3][x] == 0:
     problem.setEntry(output[3][x][3],json.dumps({"name" : output[3][x][2],"data":data }))
    else:
     problem.setOutput(output[3][x][3],json.dumps({"name" : output[3][x][2],"data":data }))

   for x in output[4]:
    if(output[4][x] == 0 or output[4][x] == 1 or output[4][x] == 2 ):
     problem.setRegister(x -1,output[4][x])
    else:
     return jsonify(result = False, err = [{'type':'danger', 'out' : "layout out of range"}])
   db.session.add(problem)
   db.session.commit()
  else:
   return jsonify(result = False, err =[{'type':'danger', 'out' : output}] )

  return jsonify(result = True)
 return jsonify(result = False)
