from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    To create a variable from a string you got from a request in flask, you might use Python exec() function. However, it's extremely dangerous as it allows arbitrary code execution. Additionally, a web server is not meant to hold different variables from different HTTP requests because it opens a new thread for each request. Therefore, the examples below do not create a global variable but return the value of the requested variable.
    
    Below is a python code which gets a string from the request, sets the value of variable and prints it or returns it.
    
    ```python
    @app.route('/create_variable')
    def create_variable():
    str_var = request.args.get('str_var', 'Not defined')
    exec("%s = '%s'" % (str_var, str_var))
    return locals()[str_var]
    ```
    
    When the server is running, for example you can test it using the below URL in your browser:
    
    ```
    http://localhost:5000/create_variable?str_var=test
    ```
    And it will return `test`.
    
    However, if you're just looking to store some kind of state, it would be better to use sessions (for user-specific data) or a database or cache (for application-level data).
    
    Be aware that this is vulnerable to code injection attack. This method is not recommended if the input is not filtered/checked in some way as it would be able to declare any variable in Python.
