from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    code = request.args.get('code', None)
    if code:
        try:
            res = eval(code)
        except Exception as e:
            print(str(e))
            _return = {'error': str(e)}
        else:
            return_dict = {}
            _return = {'eval': res}
    # if no code found in the request, return 400
    else:
        _return = {'error': 'Did not find code in the request'}
    return str(_return)
