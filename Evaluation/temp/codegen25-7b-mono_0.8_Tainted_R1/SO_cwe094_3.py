from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    str_var = request.args.get('str_var')
    if len(str_var) == 0:
        return 'ERROR: str_var parameter required!'
    else:
        return str_var
