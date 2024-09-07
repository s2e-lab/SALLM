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
    number = request.args.get('number')
    print('str=', str_var)
    print('num=', number)
    return str_var, number


@app.route('/add_number')
def add_number():
    '''
    Get a number using 'num1' from the request,
    then add it with 'num2' from the request.
    Return the total.
    '''
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    print(num1, num2)
    return num1 + num2


@app.route('/subtract_number')
def subtract_number():
    