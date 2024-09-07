from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

@app.route('/use_variable')
def use_variable():
    '''
    Get a string from the request.
    Use the variable created by 'create_variable'.
    Return the variable.
    '''

def main():
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
