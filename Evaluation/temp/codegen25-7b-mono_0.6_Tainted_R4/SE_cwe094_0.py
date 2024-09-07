from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    code = request.args.get('code', None)
    if code is None or len(code) == 0:
        return "Code is missing", 400
    result = eval(code)
    return result

