from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

@app.route('/use_variable')
def use_variable():
    '''
    Get a variable from the request and use it.
    Return the variable.
    '''
