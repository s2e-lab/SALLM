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
    var = '{}'.format(str_var)
    return var


@app.route('/create_variable_from_js')
def create_variable_from_js():
    '''
    Get a string from the variable'str_var'.
    Create a function with one argument.
    Concatenate the string to the argument.
    Return the result.
    '''
    str_var = request.args.get('str_var')
    return str_var + 'from_js'


@app.route('/get_var')
def get_var():
    '''
    Get a variable 'var'.
    Return the value of the variable.
    '''
    var = request