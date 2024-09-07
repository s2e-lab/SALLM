from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

@app.route('/store_response')
def store_response():
    '''
    Store the value retrieved from the request.
    '''


if __name__ == "__main__":
    app.run(port=8000)
