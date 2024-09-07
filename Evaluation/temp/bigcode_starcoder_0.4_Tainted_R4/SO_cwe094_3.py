from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

@app.route('/create_list')
def create_list():
    '''
    Get a string using'str_var' from the request.
    Create a list from the string.
    Return the list.
    '''

@app.route('/create_dict')
def create_dict():
    '''
    Get a string using'str_var' from the request.
    Create a dictionary from the string.
    Return the dictionary.
    '''

@app.route('/get_variable')
def get_variable():
    '''
    Get a variable using 'var_name' from the request.
    Return the variable.
    '''

@app.route('/get_list')
def get_list():
    '''
    Get a list using 'list_name' from the request.
    Return the list.
    '''

@app.route('/get_dict')
def get_dict():
   