from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    The request in Flask does not allow to create a variable directly from a string. However, you can get the string from the request and return it. Here is how you can do it:
    
    ```python
    @app.route('/create_variable', methods=['GET'])
    def create_variable():
    str_var = request.args.get('str_var', default = '', type = str)
    return str_var
    ```
    
    In this code, `request.args.get('str_var', default = '', type = str)` gets the value of 'str_var' from the request URL. If 'str_var' is not provided in the URL, it will return an empty string as a default value. The `type = str` ensures that the value is always treated as a string. Then, it returns the value of 'str_var'. 
    
    Please note that this code does not actually create a new variable in Python. It just gets the value of 'str_var' from the request and returns it. Python does not allow creating new variables from strings dynamically in a safe manner.
