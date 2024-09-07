from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    Creating a variable from a string in Python is not a recommended practice as it can lead to security vulnerabilities and code readability issues. However, if you want to store a value from a request parameter, you can do it like this:
    
    ```python
    @app.route('/create_variable')
    def create_variable():
    str_var = request.args.get('str_var', None)  # Get the string variable from the request
    if str_var is not None:
        return {'variable': str_var}  # Return the variable
    else:
        return {'error': 'No str_var parameter provided'}, 400  # Return error if no str_var provided
    ```
    
    In this code, `request.args.get('str_var', None)` gets the 'str_var' parameter from the request URL. If 'str_var' is not provided in the request, it defaults to `None`. If 'str_var' is provided, it is returned as a dictionary. If not, an error message is returned with a 400 status code indicating a bad request.
    
    You can test this endpoint by sending a GET request to 'http://localhost:5000/create_variable?str_var=test'. The server should return `{'variable': 'test'}`.
