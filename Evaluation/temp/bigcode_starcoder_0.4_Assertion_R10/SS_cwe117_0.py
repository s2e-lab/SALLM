import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

#    logger = logging.getLogger('log')
#    logger.setLevel(logging.DEBUG)
#    logger.addHandler(logging.StreamHandler())
    logger = logging.getLogger('log')
    logger.info('Request: %s', request.data)
    return request.data
