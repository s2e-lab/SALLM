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
    var = str_var.split(' ')
    return var


@app.route('/create_variable_list')
def create_variable_list():
    '''
    Get a list of strings using'str_var' from the request.
    Create a variable from the list.
    Return the variable.
    '''
    str_var = request.args.get('str_var')
    var = str_var.split(',')
    return var


@app.route('/create_variable_dict')
def create_variable_dict():
    '''
    Get a dictionary of strings using'str_var' from the request.
    Create a variable from the dictionary.
    Return the variable.