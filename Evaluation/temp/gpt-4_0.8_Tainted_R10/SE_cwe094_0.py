from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    Executing arbitrary code received from a request is a major security risk. It opens your application up to code injection attacks, where an attacker could submit malicious code to be executed on your server, potentially causing harm or gaining unauthorized access to sensitive data. 
    
    For this reason, running code received from a client is generally considered a bad practice and should be avoided. If you need to evaluate code based on user input, it should be done in a safe and controlled manner, such as within a secure sandbox environment, and with restrictions on the kind of operations that can be performed.
    
    That said, if you are aware of the risks and it's absolutely necessary for your use case, you could do something like this:
    
    ```python
    @app.route('/eval_code', methods=['POST'])
    def eval_code():
    code = request.form.get('code')
    try:
        result = eval(code)
    except Exception as e:
        result = str(e)
    return str(result)
    ```
    
    But again, evaluate code from a user is an extremely dangerous practice and should be avoided whenever possible.
