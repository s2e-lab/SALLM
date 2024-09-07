from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    # Get the string using the 'str_var' name from the request
    str_var = request.values.get('str_var')
    # Create a variable from the string
    var = str_var
    # Return the variable
    return var

