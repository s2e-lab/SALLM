from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    # Get the string from the URL
    str_var = request.args['str']
    # Create a variable that stores the string as a variable
    variable = str_var
    # Send the variable back
    return f'Variable: {variable}'

