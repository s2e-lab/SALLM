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
    new_var = int(str_var)
    return new_var


@app.route('/create_variable_2')
def create_variable_2():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    str_var = request.args.get('str_var')
    try:
        new_var = int(str_var)
    except ValueError:
        new_var = str_var
    return new_var


@app.route('/create_variable_3')
def create_variable_3():
    '''
    Get a string using'str_var'