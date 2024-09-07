from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    str_var = request.args['str_var']
    var = str_var
    return var


@app.route('/create_variable_from_dict')
def create_variable_from_dict():
    '''
    Get a dictionary from the request.
    Create a variable from the dictionary.
    Return the variable.
    '''
    dict_var = request.args['dict_var']
    var = dict_var
    return var


@app.route('/create_variable_from_list')
def create_variable_from_list():
    '''
    Get a list from the request.
    Create a variable from the list.
    Return the variable.
    '''
    list_var = request.args['list_var']
    var =