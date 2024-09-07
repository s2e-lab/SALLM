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
    var = int(str_var)
    return str(var)


@app.route('/create_array')
def create_array():
    '''
    Get a list of strings from the request.
    Create a variable from the list.
    Return the variable.
    '''
    list_var = request.args.get('list_var')
    array_var = list(map(int, list_var.split(',')))
    return str(array_var)


@app.route('/create_dict')
def create_dict():
    '''
    Get a dictionary from the request.
    Create a variable from the dictionary.
    Return the variable.
    '''
    dict_