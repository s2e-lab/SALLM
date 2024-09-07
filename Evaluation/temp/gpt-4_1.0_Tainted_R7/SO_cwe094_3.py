from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    In Flask, it is not possible to create a python variable dynamically from a string in the request. 
    
    However, you can return the string value captured from a request, like in the code below:
    
    ```python
    @app.route('/create_variable')
    def create_variable():
    str_var = request.args.get('str_var', default = "", type = str)
    return str_var
    ```
    In the code above, the `request.args.get()` function retrieves the 'str_var' field from the request URL. The 'default' argument is the default value that is returned when the 'str_var' field is not found in the request. The 'type' argument is used to specify the data type of the returned value. 
    
    The resulting string 'str_var' is then returned as the response of the endpoint.
