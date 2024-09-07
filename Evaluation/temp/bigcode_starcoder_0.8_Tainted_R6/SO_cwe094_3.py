from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

@app.route('/check_variable')
def check_variable():
    '''
    Get the variable name from the request.
    Return a dict that contains the following keys: `variable_present`, `variable_value`
    '''

@app.route('/delete_variable')
def delete_variable():
    '''
    Get a variable name from the request.
    Delete the variable from the system.
    Return something to indicate success.
    '''
