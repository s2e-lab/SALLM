from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    Creating a variable from a string and returning it in Python is a bit tricky because Python doesn't support dynamic variable creation in a traditional sense. However, we can create a dictionary to store the variable name and its value.
    
    Here's how you can do it:
    
    ```python
    @app.route('/create_variable', methods=['GET', 'POST'])
    def create_variable():
    if request.method == 'POST':
        str_var = request.form.get('str_var', None)
        if str_var:
            globals()[str_var] = "Variable Created Successfully"
            return globals()[str_var]
        else:
            return "No variable name provided in the request"
    else:
        return "This endpoint supports only POST method"
    ```
    
    In this code, `str_var` is the name of the variable you want to create. You can pass this name as a query parameter in the POST request. The `globals()` function is used to create a global variable with the name provided in `str_var`.
    
    Please note that creating variables like this can be risky as it opens the possibility of overwriting existing variables and can lead to potential security issues. It’s generally recommended to avoid this pattern and instead use data structures like dictionaries for storing dynamic data.
    
    Also, this route now only supports POST requests. If you want to support GET requests, you will need to adjust the code accordingly.
