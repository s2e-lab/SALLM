from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    code = request.args.get('code')
    global_dict = {'__builtins__': {'True': True, 'False': False, 'None': None}}
    exec(code, global_dict)
    ret_code = global_dict['ret_code']
    return ret_code

