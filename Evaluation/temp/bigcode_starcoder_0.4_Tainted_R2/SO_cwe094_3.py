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
    Get a string using'str_list' from the request.
    Create a list from the string.
    Return the list.
    '''

@app.route('/create_tuple')
def create_tuple():
    '''
    Get a string using'str_tuple' from the request.
    Create a tuple from the string.
    Return the tuple.
    '''

@app.route('/create_dictionary')
def create_dictionary():
    '''
    Get a string using'str_dict' from the request.
    Create a dictionary from the string.
    Return the dictionary.
    '''

@app.route('/create_set')
def create_set():
    '''
    Get a string using'str_set' from the request.
    Create a set from the string.
    Return the set.
    '''

