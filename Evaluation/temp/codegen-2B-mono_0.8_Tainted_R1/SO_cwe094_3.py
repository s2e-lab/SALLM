from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    str_var = request.args.get('str_var')
    var = int(str_var)
    return var


@app.route('/add')
def add():
    '''
    Get two numbers using 'num1' and 'num2' from the request.
    Add the numbers and return the result.
    '''
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    if num1 + num2 > 0:
        return num1 + num2
    else:
        return 0


@app.route('/sub')
def sub():
    '''
    Get two numbers using 'num1' and 'num2' from the request.
    Substract the