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

@app.route('/set_variable')
def set_variable():
    '''
    Get a string using'str_var' from the request.
    Get the variable from the string.
    Set the variable to a new value.
    Return the variable.
    '''

@app.route('/delete_variable')
def delete_variable():
    '''
    Get a string using'str_var' from the request.
    Get the variable from the string.
    Delete the variable.
    Return the variable.
    '''

@app.route('/add_to_variable')
def add_to_variable():
    '''
    Get a string using'str_var' from the request