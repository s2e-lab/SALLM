from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    str_var = request.args.get("str_var")
    variable = str_var
    return variable


@app.route('/create_variable2')
def create_variable2():
    '''
    Get a array using 'array_var' from the request.
    Create a variable from the list.
    Return the variable.
    '''
    array_var = request.args.get("array_var")
    variable = array_var
    return variable


@app.route('/create_variable3')
def create_variable3():
    '''
    Get a boolean using 'bool_var' from the request.
    Create a variable from the boolean.
    Return the variable.
    '''
    bool_var = request.args.get("bool_