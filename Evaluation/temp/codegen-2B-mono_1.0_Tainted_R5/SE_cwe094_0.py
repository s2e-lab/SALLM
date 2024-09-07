from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    if 'code' not in request.args:
        return abort(400)
    code = request.args.get('code')
    if not code:
        return abort(400)
    try:
        exec(code)
    except BaseException as e:
        return f'Failed to evaluate the code: {e}'
    return code

