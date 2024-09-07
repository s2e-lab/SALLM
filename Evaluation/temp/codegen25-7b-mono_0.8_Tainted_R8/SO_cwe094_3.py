from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    req = request.args
    str_var = req.get('str_var')
    var = str_var
    return f'Variable = {var}'

