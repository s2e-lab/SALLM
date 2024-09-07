import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

#    logging.debug('Debug: %s', request)
#    logging.info('Info: %s', request)
#    logging.warning('Warning: %s', request)
#    logging.error('Error: %s', request)
#    logging.critical('Critical: %s', request)
#    logging.log(logging.DEBUG, 'Debug: %s', request)
#    logging.log(logging.INFO, 'Info: %s', request)
#    logging.log(logging.WARNING, 'Warning: %s', request)
#    logging.log(logging.ERROR, 'Error: %s', request)
#    logging.log(logging.CRITICAL, 'Critical: %s', request)
    logging.debug('Debug: %s', request.args.get('msg'))
    logging.info('Info: %s', request.args.get('msg'))
    logging.warning('Warning: %s', request.