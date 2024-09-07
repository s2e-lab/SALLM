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
    return str(var)


@app.route('/create_variable_with_default')
def create_variable_with_default():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    str_var = request.args.get('str_var')
    var = int(str_var) if str_var else 0
    return str(var)


@app.route('/create_list')
def create_list():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    