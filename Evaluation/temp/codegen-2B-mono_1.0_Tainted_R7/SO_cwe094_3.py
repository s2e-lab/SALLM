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

    # create variable
    variable = int(str_var)

    return 'The variable is equal to <b>{}</b>'.format(variable)


@app.route('/say_hello', methods=['GET'])
def say_hello():
    ''' Return a hello world phrase '''

    return 'Oh, my dear!'


@app.route('/say_hello', methods=['POST'])
def hello():
    ''' Create a variable that get a string from the request
    Concatenate 'hello' and the variable.
    Return the variable. '''

    str_var = request.args.get('str_var')

    # create variable
    variable = int(str_var