from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    #'str_var' should be passed by POST request.
    str_var = request.args.get('str_var', None)
    
    my_var = None
    if str_var:
        my_var = str_var
    
    return '<h1>Variable with value =' + str(my_var) + '</h1>'


@app.route('/create_variable/<my_var>')
def create_variable_by_name(my_var):
    return '<h1>Variable with value =' + str(my_var) + '</h1>'


@app.route('/create_variable/<my_var>/<some_var>')
def create_variable_with_variables(my_var