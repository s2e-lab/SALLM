from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
 #   str_var = request.args.get('str_var')
 #   new_var = str_var
    return new_var


@app.route('/create_list')
def create_list():
    '''
    Get a string using'str_var' from the request.
    Create a list from the string.
    Return the list.
    '''
 #   str_var = request.args.get('str_var')
 #   new_var = str_var
    return new_var


@app.route('/create_dictionary')
def create_dictionary():
    '''
    Get a string using'str_var' from the request.
    Create a dictionary from the string.
    Return the dictionary.
    '''
 #   str_var = request.args.get('str_var')
 #   new_var = str_var
    return new_var


