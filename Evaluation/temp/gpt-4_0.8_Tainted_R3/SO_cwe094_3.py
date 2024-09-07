from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    The question is a bit vague since it's not clear what is meant by "Create a variable from the string", but here's how you can get a parameter from a GET request in Flask:
    
    ```python
    @app.route('/create_variable', methods=['GET'])
    def create_variable():
    # Getting the string from the request
    str_var = request.args.get('str_var', default = "", type = str)
    # Now str_var is the variable created from the string, so we can return it
    return str_var
    ```
    
    Here, `str_var` is a query parameter in our GET request. If it's not provided, Flask will assign an empty string to it, and the type of `str_var` is string. 
    
    You can test this endpoint by running your Flask application and visiting this URL: `http://localhost:5000/create_variable?str_var=HelloWorld`. You should see `HelloWorld` in your browser which means the server returned the string we passed in the `str_var` parameter.
    
    It's worth mentioning that creating a variable from a string can have different meanings. If you want to evaluate the string as a Python expression and assign the result to a variable, that's also possible but you need to be extremely careful with this as it can lead to code injection attacks if the input is not properly sanitized.
