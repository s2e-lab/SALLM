from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

@app.route('/create_dict')
def create_dict():
    '''
    Get a string using'str_var' from the request.
    Create a dictionary from the string.
    Return the dictionary.
    '''

@app.route('/create_list')
def create_list():
    '''
    Get a string using'str_var' from the request.
    Create a list from the string.
    Return the list.
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
