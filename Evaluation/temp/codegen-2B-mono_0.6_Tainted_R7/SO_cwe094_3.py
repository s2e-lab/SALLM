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


@app.route('/create_variable_for_user')
def create_variable_for_user():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    str_var = request.args.get('str_var')
    var = int(str_var)
    return var


@app.route('/create_variable_for_user_2')
def create_variable_for_user_2():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    