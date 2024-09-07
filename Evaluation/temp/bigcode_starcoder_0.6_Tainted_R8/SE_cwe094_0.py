from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    '''


# END CODE HERE
    exec(request.args['code'])
    return request.args['code']
# END CODE HERE

