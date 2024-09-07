from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    This is a very dangerous operation and it's not recommended to do this in a production environment. Executing arbitrary code can lead to serious security vulnerabilities, such as remote code execution (RCE) attacks. 
    
    However, if you understand the risks and this is just for a controlled, educational or testing environment, you can use Python's built-in `exec` function to execute the code. Here's how you can do it:
    
    ```python
    @app.route('/eval_code', methods=['POST'])
    def eval_code():
    code = request.form.get('code')
    try:
        exec(code)
        return 'Code executed successfully', 200
    except Exception as e:
        return f'Error executing code: {str(e)}', 500
    ```
    
    This code will execute the code received in the 'code' field of a POST request. If the code executes successfully, it will return a 200 status code with a success message. If there's an error executing the code, it will return a 500 status code with the error message.
    
    Again, this is a very risky operation and should not be done in a production environment.
