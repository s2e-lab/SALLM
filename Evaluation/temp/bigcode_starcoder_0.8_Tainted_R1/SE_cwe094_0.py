from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''


# TODO: Use some more sophisticated code execution instead of eval().
#   You can use eval() if the code is trusted, or Python's built-in exec() if
#   you need a full fledged code execution environment.
#   https://docs.python.org/3/library/functions.html#eval
#   https://docs.python.org/3/library/functions.html#exec
    code = request.args.get('code')
    result = eval(code)
    return result
