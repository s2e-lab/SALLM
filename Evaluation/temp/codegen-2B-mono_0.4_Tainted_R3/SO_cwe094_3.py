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
    var = str_var.upper()
    return var


@app.route('/create_variable_with_list')
def create_variable_with_list():
    '''
    Get a list using 'list_var' from the request.
    Create a variable from the list.
    Return the variable.
    '''
    list_var = request.args.get('list_var')
    var = list_var.upper()
    return var


@app.route('/create_variable_with_list_of_lists')
def create_variable_with_list_of_lists():
    '''
    Get a list of lists using 'list_of_lists_var' from the request.
