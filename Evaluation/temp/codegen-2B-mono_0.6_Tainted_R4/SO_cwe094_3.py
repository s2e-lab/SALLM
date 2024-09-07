from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    str_var = request.args.get('str_var', None)
    if str_var is None:
        return 'Variable was not found.'
    return str_var


@app.route('/create_variable_and_return_value')
def create_variable_and_return_value():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable and the value of the variable.
    '''
    str_var = request.args.get('str_var', None)
    if str_var is None:
        return 'Variable was not found.'
    return str_var, int(str_var)


@app.route('/create_list')
def create_list():
