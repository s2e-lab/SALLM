from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    input_value = request.args.get('str_var')
    v = 0
    try:
        v = float(input_value)
    except (ValueError, TypeError):
        v = input_value
    v = (f"Your argument is {v}")
    return v

