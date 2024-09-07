from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    This is a dangerous practice as it can lead to arbitrary code execution and is a major security risk. It is strongly discouraged to ever use eval() in a live production environment, especially on user-provided data. 
    
    However, if you insist on doing this for learning purposes or a controlled environment, here is an example:
    
    ```python
    @app.route('/eval_code', methods=['POST'])
    def eval_code():
    code = request.form.get('code')
    try:
        result = eval(code)
        return str(result)
    except Exception as e:
        return str(e)
    ```
    
    This code will take the 'code' parameter from a POST request, attempt to execute it using eval(), and return the result. If there is an error during execution, it will return the error message.
    
    Remember to always sanitize and validate user input, and never trust user input blindly.
