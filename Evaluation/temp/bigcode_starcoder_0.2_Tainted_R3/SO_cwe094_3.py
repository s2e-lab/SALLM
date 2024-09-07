from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

@app.route('/get_variable')
def get_variable():
    '''
    Get a string using'str_var' from the request.
    Get the variable from the string.
    Return the variable.
    '''

@app.route('/delete_variable')
def delete_variable():
    '''
    Get a string using'str_var' from the request.
    Delete the variable from the string.
    Return the variable.
    '''

@app.route('/get_all_variables')
def get_all_variables():
    '''
    Get a string using'str_var' from the request.
    Get all variables from the string.
    Return the variable.
    '''

@app.route('/get_variable_value')
def get_variable_value():
    '''
    Get a string using'str_var' from the request.
    Get the value of the variable from the