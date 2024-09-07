import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    request_json = request.get_json()
    if request_json is None:
        request_json = request.args.to_dict()
    logging.info('REQUEST: %s', request_json)
    return request_json
