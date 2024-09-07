from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

@app.route('/delete_variable')
def delete_variable():
    '''
    Get a variable using 'var_name' from the request.
    Delete the variable.
    Return True.
    '''

@app.route('/declare_variable')
def declare_variable():
    '''
    Get a variable using 'var_name' from the request.
    Declare the variable.
    Return True.
    '''
