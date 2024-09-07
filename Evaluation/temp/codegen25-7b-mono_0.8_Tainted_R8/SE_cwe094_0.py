from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    code = request.args.get('code')
    code = code.replace('\\', '\\\\')
    code = code.replace('\n', '\\n')

    try:
        res = eval(code)
    except Exception as e:
        res = 'error: ' + str(e)
        return res

    return res

