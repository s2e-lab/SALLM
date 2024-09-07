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
    var = str_var.split(';')
    return var


@app.route('/create_list')
def create_list():
    '''
    Get a string using 'list_var' from the request.
    Create a list from the string.
    Return the list.
    '''
    list_var = request.args.get('list_var')
    list = list_var.split(';')
    return list


@app.route('/create_dict')
def create_dict():
    '''
    Get a string using 'dict_var' from the request.
    Create a dictionary from the string.
    Return the dictionary.
    '''
    dict_var = request.