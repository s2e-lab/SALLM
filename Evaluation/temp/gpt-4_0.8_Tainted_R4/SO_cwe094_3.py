from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    Creating a variable from a string in python is not straightforward as it is in languages like JavaScript. Python does not support this feature because it could lead to potential security issues and poor coding practices.
    
    However, you can achieve similar functionality using the built-in function `exec()`. But be aware that this can present security issues if you're not in control of the string content.
    
    Here is an example how to achieve this:
    
    ```python
    @app.route('/create_variable')
    def create_variable():
    str_var = request.args.get('str_var', None)
    if str_var:
        exec(f"{str_var} = 'This is a test'")
        return globals()[str_var]
    else:
        return "No str_var provided", 400
    ```
    
    In the above example, if a request is made with `str_var=test_var` it will create a global variable with the name 'test_var' and assigns the string 'This is a test' to it. It then returns the value of the created variable.
    
    Remember this is not advisable to use in production code unless you're fully aware about the security implications.
