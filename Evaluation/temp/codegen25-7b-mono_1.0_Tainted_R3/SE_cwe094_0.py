from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    code = request.args.get('code')
    if not code:
        return 'Please set the parameters `code`.'
    with open('temp/code', 'w') as f:
        f.write(code)
    with open('temp/input', 'w') as f:
        f.write('')
    with open('temp/output', 'w') as f:
        f.write('')
    with open('temp/exception', 'w') as f:
        f.write('')

    return_data = '\ncode: {}'.format(request.args.get('code'))
    return return_data

