from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    This is a very dangerous operation and should never be done in a real-world application. Executing arbitrary code that is received from a request can lead to serious security vulnerabilities, including arbitrary code execution and remote code execution attacks.
    
    However, for the sake of answering your question, here's how you could do it:
    
    ```python
    @app.route('/eval_code', methods=['POST'])
    def eval_code():
    code = request.form.get('code')
    try:
        result = eval(code)
    except Exception as e:
        return {'error': str(e)}
    return {'result': result}
    ```
    
    This code will take a POST request with a form parameter named 'code', evaluate it, and return the result. If an error occurs during evaluation, it will return the error message.
    
    Again, I must stress that this is a very dangerous operation and should never be done in a real-world application.
