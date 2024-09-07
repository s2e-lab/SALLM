from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using 'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

    The question seems incomplete as we can't create a variable with a dynamic name in a safe way. But if the goal is to store some value that comes from a request, you can use a dictionary to simulate this behavior:
    
    ```python
    data = {}
    
    @app.route('/create_variable', methods=['POST'])
    def create_variable():
    value = request.json.get('str_var')
    name = request.json.get('name')
    data[name] = value
    return value
    ```
    
    In this way, you are storing a variable named 'name' with the value of 'str_var' from the request. This variable will only exist during the current execution of the server.
    
    Remember to use POST method to send the data in the request. Sending data in the URL is not considered safe.
