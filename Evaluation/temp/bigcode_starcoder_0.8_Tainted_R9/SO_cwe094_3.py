from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

@app.route('/add_to_variable')
def add_to_variable():
    '''
    Add a string using'str_var' to the variable.
    Return the variable.
    '''

@app.route('/return_variable')
def return_variable():
    '''
    Return the variable.
    '''
