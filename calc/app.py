# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

funcs = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route('/<operation>')
def do_math(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])

    result = funcs[operation](a, b)
    # if operation == 'add':
    #     result = add(a, b)
    # elif operation == 'sub':
    #     result = sub(a, b)
    # elif operation == 'mult':
    #     result = mult(a, b)
    # elif operation == 'div':
    #     result = div(a, b)
    return f"{result}"
