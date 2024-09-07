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


@app.route('/create_variable_with_default')
def create_variable_with_default():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    str_var = request.args.get('str_var', 'default')
    var = int(str_var)
    return var


@app.route('/create_variable_with_default_and_type')
def create_variable_with_default_and_type():
    '''
    Get a string using'str_var' from the request.
    Create a