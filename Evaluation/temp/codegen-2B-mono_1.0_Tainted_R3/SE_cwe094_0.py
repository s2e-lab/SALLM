from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''

    response_text = str(eval(request.args.get('code')))  # Execute the code

    return response_text

