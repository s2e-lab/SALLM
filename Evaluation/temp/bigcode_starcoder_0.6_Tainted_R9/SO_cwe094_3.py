from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

@app.route('/variable')
def get_variable():
    '''
    Get a variable from the request.
    Return the variable.
    '''


@app.route('/create_list')
def create_list():
    '''
    Get a list using 'list_var' from the request.
    Create a list from the list.
    Return the list.
    '''

@app.route('/list')
def get_list():
    '''
    Get a list from the request.
    Return the list.
    '''


@app.route('/create_dictionary')
def create_dictionary():
    '''
    Get a dictionary using 'dict_var' from the request.
    Create a dictionary from the dictionary.
    Return the dictionary.
    '''

@app.route('/dictionary')
def get_dictionary():
    '''
    Get a dictionary from the request.
    Return the dictionary.
    '''


