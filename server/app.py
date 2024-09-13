#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:integer>')
# def count(integer):
#     integer_range = range(integer)
#     for int in integer_range:
#         return f'{int}\n'
def count(integer):
    count = f''
    for n in range(integer):
        count += f'{n}\n'
    return count


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "div":
        return str(num1 / num2)
    elif operation == "%":
        return str(num1 % num2)
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)

