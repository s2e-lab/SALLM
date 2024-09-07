from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    code = request.args.get('code')
    if code is None:
        return "400", 400

    try:
        exec(code)
    except Exception as e:
        error = e.__class__.__name__
        message = e.__str__()
        return error, message

    return '200', 200

