from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    # Get the Python script from request body
    body_code = request.get_json()['code']

    # Execute it without the `print`. It must return a Python "string"
    out = compile(body_code, "<string>", 'exec')
    # Return code and return
    return 'Code executed, here is the return:'+ str(eval(out))

