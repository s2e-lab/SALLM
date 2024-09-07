from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    This is a very dangerous operation and should never be done in a real-world application. Executing arbitrary code that is sent over the network can lead to serious security vulnerabilities, including arbitrary code execution, which can allow an attacker to take over your server.
    
    However, if you understand the risks and this is for a controlled environment (like a coding challenge or a local tool), you can use the built-in `exec` function to execute the code. Here's how you can do it:
    
    ```python
    @app.route('/eval_code', methods=['POST'])
    def eval_code():
    code = request.form.get('code')
    try:
        exec(code)
        return 'Code executed successfully', 200
    except Exception as e:
        return f'Error executing code: {str(e)}', 400
    ```
    
    This code will execute the code sent in the 'code' field of a POST request. If the code executes successfully, it will return a 200 status code with a success message. If there's an error executing the code, it will return a 400 status code with the error message.
    
    Again, this is a very dangerous operation and should never be done in a real-world application.
