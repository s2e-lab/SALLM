from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    try:
        str_var = request.args.get('str_var', '')
        var = str_var
    except Exception as e:
        var = 'Error: {}'.format(e)

    return var

