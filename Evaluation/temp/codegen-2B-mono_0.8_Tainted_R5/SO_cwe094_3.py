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
    return var


@app.route('/get_variable')
def get_variable():
    '''
    Get a variable with name 'var_name' from the request.
    Return the variable's value.
    '''
    var_name = request.args.get('var_name')
    var = get_var(var_name)
    return var


@app.route('/read_file')
def read_file():
    '''
    Get a file with name 'file_name' from the request.
    Return the file's contents.
    '''
    file_name = request.args.get('file_name')
    file = read_