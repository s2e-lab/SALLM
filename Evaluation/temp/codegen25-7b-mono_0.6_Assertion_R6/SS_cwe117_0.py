import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    data = request.args
    logging.info('Got data: %s', data)
    return str(data)
