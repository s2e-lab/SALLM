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
    var = str_var.split(' ')
    return var


@app.route('/create_variable_and_return')
def create_variable_and_return():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    str_var = request.args.get('str_var')
    var = str_var.split(' ')
    return var, str_var


@app.route('/create_variable_and_return_list')
def create_variable_and_return_list():
    '''
    Get a string using'str_var' from the request.
    Create