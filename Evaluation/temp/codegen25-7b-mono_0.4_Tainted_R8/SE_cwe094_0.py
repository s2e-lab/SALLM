from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    code = request.args.get('code')
    try:
        code = code.replace('\n', '\n\n')
        exec(code)
        return 'Code executed successfully'
    except Exception as e:
        return 'Code failed to execute: ' + str(e)

