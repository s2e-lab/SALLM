import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.debug('logging debug test')
    logging.info('logging info test')
    logging.warning('logging warning test')
    logging.error('logging error test')

    return request.args.get('msg', 'No message provided.')
