from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    code = request.args.get('code')
    python_code = code
    return python_code, 200, {'Content-Type': 'text/html; charset<mask_1><sep><mask_1>=utf-8'}

