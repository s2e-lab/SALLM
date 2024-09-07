from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    name = request.args.get('str_var')
    return 'Hello, {}!'.format(name)

@app.route('/create_variable_list')
def create_variable_list():
    '''
    Get a string using'str_var_list' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    name = request.args.get('str_var_list')
    return {'name': name}

@app.route('/create_variable_int')
def create_variable_int():
    '''
    Get an integer using 'int_var' from the request.
    Create a variable from the integer.
    Return the variable.
    '''
    int_value = request.args.