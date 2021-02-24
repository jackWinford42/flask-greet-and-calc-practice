# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request 

app = Flask(__name__)

@app.route("/add")
@app.route("/math/add")
def route_add():
    a = request.args["a"]
    b = request.args["b"]
    return str(add(int(a), int(b)))

@app.route("/sub")
@app.route("/math/sub")
def route_subtract():
    a = request.args["a"]
    b = request.args["b"]
    return str(sub(int(a), int(b)))

@app.route("/mult")
@app.route("/math/mult")
def route_multiply():
    a = request.args["a"]
    b = request.args["b"]
    return str(mult(int(a), int(b)))

@app.route("/div")
@app.route("/math/div")
def route_divide():
    a = request.args["a"]
    b = request.args["b"]
    return str(div(int(a), int(b)))
