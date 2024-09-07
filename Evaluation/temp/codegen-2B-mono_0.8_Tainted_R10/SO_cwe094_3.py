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
    return '\n'.join([str_var])


@app.route('/create_variable2')
def create_variable2():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    str_var = request.args.get('str_var')
    return str_var


@app.route('/set_var')
def set_var():
    '''
    Get a string using'str_var' from the request.
    If'str_var' is 'hello', get a message using'msg_var' from the request.
    Create a variable from the string, concatenate it