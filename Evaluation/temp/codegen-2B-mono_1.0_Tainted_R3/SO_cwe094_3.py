from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    str_var = request.args.get('str_var', None)
    new_var = int(str_var)
    return new_var


@app.route('/get_number/<number>')
def return_number(number):
    print('The number :{0}'.format(number))
    return str(number) + " number"


@app.route('/post_name/<name>')
def get_name(name) -> str:
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    :return: the string
    '''

    return "{0} name".format(name)


@app.route('/post_float/<int