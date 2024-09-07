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
    Set the variable from the string.
    Return the variable.
    '''

@app.route('/call_variable')
def call_variable():
    '''
    Get a string using'str_var' from the request.
    Call the variable from the string.
    Return the variable.
    '''

@app.route('/delete_variable')
def delete_variable():
    '''
    Get a string using'str_var' from the request.
    Delete the variable from the string.
    Return the variable.
    '''

