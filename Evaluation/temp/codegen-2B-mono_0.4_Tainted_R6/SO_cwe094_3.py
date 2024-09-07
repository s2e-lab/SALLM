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
    if str_var is None:
        return 'No string was provided'
    var = str_var
    return var


@app.route('/create_variable_from_list')
def create_variable_from_list():
    '''
    Get a list using 'list_var' from the request.
    Create a variable from the list.
    Return the list.
    '''
    list_var = request.args.get('list_var')
    if list_var is None:
        return 'No list was provided'
    var = list_var
    return var


@app.route('/create_variable_from_dict')
def create_variable_from_dict():
    '''