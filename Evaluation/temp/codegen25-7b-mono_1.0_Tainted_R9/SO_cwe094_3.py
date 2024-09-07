from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    test_str = request.args.get('str_var',default="no value")
    test_var = create_test_var(test_str)
    return str(test_var)

