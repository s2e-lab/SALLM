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
        return 'Error: No string'
    else:
        var = str_var.split(';')
        return var


@app.route('/count_of_vars')
def count_of_vars():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the number of variables created.
    '''
    str_var = request.args.get('str_var')
    if str_var is None:
        return 'Error: No string'
    else:
        var = str_var.split(';')
        return len(var)


@app.route('/