from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
# Implement this function.
    var = 'new var'
    return var

if __name__ == '__main__':
    app.run(debug=True)