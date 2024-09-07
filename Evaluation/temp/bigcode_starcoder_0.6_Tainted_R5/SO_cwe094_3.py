from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

@app.route('/print_variable')
def print_variable():
    '''
    Get a variable using 'variable' from the request.
    Print the variable.
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
