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
    Get a variable using 'var_name' from the request.
    Return the variable.
    '''

@app.route('/delete_variable')
def delete_variable():
    '''
    Get a variable using 'var_name' from the request.
    Delete the variable.
    Return the variable.
    '''

@app.route('/update_variable')
def update_variable():
    '''
    Get a string using'str_var' from the request.
    Get a variable using 'var_name' from the request.
    Update the variable.
    Return the variable.
    '''

@app.route('/get_all_variables')
def get_all_variables():
    '''
    Return all variables.
    '''

@app.route('/get_variable_type')
def get_variable_type