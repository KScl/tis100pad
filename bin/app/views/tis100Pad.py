from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify

from app import db
from app.model.solution import Solution

mod = Blueprint('pad', __name__, url_prefix='/')

@mod.route('/', defaults={'path': ''})
@mod.route('<path:path>')
def root(path):
 return render_template("PadView.html")

@mod.route('solution/<int:solution>', methods=['POST','GET'])
def getSolution(solution):
 output = [[]]
 return jsonify(solution = Solution.query.filter_by(id = solution).first().getRegistersGrid())

@mod.route('save', methods=['POST','GET'])
def save():
 nodes = request.get_json().get("nodes")
 solution = Solution( 
  nodes[0][0].get("text"),nodes[0][1].get("text"),nodes[0][2].get("text"),nodes[0][3].get("text"),
  nodes[1][0].get("text"),nodes[1][1].get("text"),nodes[1][2].get("text"),nodes[1][3].get("text"),
  nodes[2][0].get("text"),nodes[2][1].get("text"),nodes[2][2].get("text"),nodes[2][3].get("text"),0,0)
 db.session.add(solution)
 db.session.flush()
 db.session.commit()
 return jsonify(id= solution.id)