from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    code = request.args['code']

    print(code)

    compiled_code = compile(code, '<string>', 'exec')

    codeobj = eval(compiled_code)
    if callable(codeobj) or hasattr(codeobj, "__name__") or isinstance(codeobj, (int, float, str)):
        return codeobj

    return codeobj.execute()

