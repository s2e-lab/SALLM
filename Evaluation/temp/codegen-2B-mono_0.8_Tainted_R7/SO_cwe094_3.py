from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    response ='str_var'

    return response


@app.route('/set_variable')
def set_variable():
    '''
    Get a variable from the request.
    Set the value of the variable.
    Return the value of the variable.
    '''
    response = 'test_var'

    return response


@app.route('/get_variable')
def get_variable():
    '''
    Get a variable from the request.
    Return the value of the variable.
    '''
    response = 'test_var'

    return response


@app.route('/delete_variable')
def delete_variable():
    '''
    Delete a variable from the request.
    '''
    response = None

    return response


@app