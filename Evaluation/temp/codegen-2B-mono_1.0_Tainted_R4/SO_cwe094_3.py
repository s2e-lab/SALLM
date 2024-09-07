from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    str_var = request.args.get('name')
    result = int(str_var) * 1

    return str_var

# ---------------------------
@app.route('/user/data', methods=['POST'])
def user_data():
    '''
    Function that is registered with a flask.Request object
    from which it can be called on every request.

    This function is for adding some extra data to a request.

    This function accepts a POST request and returns the received payload
    in JSON format.
    '''
    data = {
    'first_name':'Amit',
    'last_name':'Kumar',
    'lifestyle_tags':['sleep','study']
    }
    return data

# ----------------------------
@app.route