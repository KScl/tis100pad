from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify, redirect
from app import db
from app.model.solution import Solution
from app.model.problem import Problem
from app.model.account import Account

from multiprocessing import Process,Queue

import json
import lupa
import string
import psutil, os

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

@mod.route('/problem/<string:identifier>',methods=['POST'])  
def getProblem(identifier):
 problem = Problem.query.filter_by(identifier = identifier).first()
 if problem == None:
  return jsonify(result = False)
 else:
  return jsonify(result = True,identifier = problem.identifier, description = problem.description, code = problem.script)

def handler(code,result):
 print "running"
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
   ''' + code + '''
   return get_name(), get_description(), get_streams(), get_layout()
   ''')
 if(output[0] == None):
  result.put(False)
  result.put([{'type':'danger', 'out' : output[1]}])
  return

 name = output[1]
 if not type(name) is unicode:
  result.put(False)
  result.put([{'type':'danger', 'out' : "invalid data type for name"}])
 
 descriptors = []
 for x in output[2]:
  if not type(output[2][x]) is unicode:
   result.put(False)
   result.put([{'type':'danger', 'out' : "description must be a string"}])
  descriptors.append(output[2][x])

 streams = []
 for x in output[3]:
  data = []
  for y in output[3][x][4]:
   if not type(output[3][x][4][y]) is int:
    result.put(False)
    result.put([{'type':'danger', 'out' : "input or output has an invalid data type for" + output[3][x][2] }])

   if output[3][x][4][y] > 999 or output[3][x][4][y] < -999:
    result.put(False)
    result.put([{'type':'danger', 'out' : "input or output are out of bound [-999,999] for " + output[3][x][2] }])
    return
   data.append(output[3][x][4][y])

  if not type(output[3][x][2]) is unicode:
   result.put(False)
   result.put([{'type':'danger', 'out' : "input or output has an invalid data type for" }])
   return

  if not type(output[3][x][3]) is int:
   result.put(False)
   result.put([{'type':'danger', 'out' : "input or output has an invalid data type for" + output[3][x][2] }])
   return

  if not type(output[3][x][1]) is int:
   result.put(False)
   result.put([{'type':'danger', 'out' : "input or output has an invalid data type for" + output[3][x][2] }])
   return

  if output[3][x][3] < 1 or output[3][x][3] > 4:
   result.put(False)
   result.put([{'type':'danger', 'out' : output[3][x][2] + ":index out of range"}])
   return   

  if not (output[3][x][1] == 1 or output[3][x][1] == 0):
   result.put(False)
   result.put([{'type':'danger', 'out' : "Invalid STREAM_INPUT/STREAM_OUTPUT"}])
   return   
  streams.append({'type':output[3][x][1],'name':output[3][x][2],'index':output[3][x][3],'data':data})

 layout = []
 for x in output[4]:
  if not ((output[4][x]+1)%1 == 0):
   result.put(False)
   result.put([{'type':'danger', 'out' : "layout has invalid data types"}])
   return

  if(output[4][x] == 0 or output[4][x] == 1 or output[4][x] == 2 ):
   layout.append(output[4][x])
  else:
   result.put(False)
   result.put([{'type':'danger', 'out' : "layout has invalid data"}])
   return
 result.put(True)
 result.put({"name":name,"descriptor":descriptors,"stream":streams,"layout":layout})



@mod.route('/submit.json',methods=['POST'])
def submit():
 if session.has_key("account.id") == False:
  return jsonify(result = False, err = [{'type':'danger', 'out' : "Please Login "}])

 if Problem.query.filter_by(identifier = request.get_json().get("identifier")).first() == None:
  result = Queue()
  t = Process(target=handler, args=(request.get_json().get("code"),result))
  t.start()
  t.join(2)
  if t.is_alive():
   process = psutil.Process(t.pid)
   process.kill()
   process.wait()
   return jsonify(result = False, err =[{'type':'danger', 'out' : "Process terminated"}] )

  if(result.get() == False):
   return jsonify(result = False, err = result.get())
  else:
   output = result.get()
   problem = Problem()
   problem.name = output["name"]
   problem.identifier = request.get_json().get("identifier")
   problem.description = request.get_json().get("description")
   problem.script = request.get_json().get("code")
   problem.descriptor = json.dumps(output["descriptor"])
   problem.userId = session["account.id"]
   for item in output["stream"]:
    if item["type"] == 0:
     problem.setEntry(item["index"],item["name"],item["data"])
    else:
     problem.setOutput(item["index"],item["name"],item["data"])
   
   index = 0
   for item in output["layout"]:
    problem.setRegister(index,item)
    index += 1

   db.session.add(problem)
   db.session.commit()
   return jsonify(result = True)