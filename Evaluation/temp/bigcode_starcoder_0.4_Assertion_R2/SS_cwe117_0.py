import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

#    logging.debug('A value for debugging')
#    logging.info('A value for information')
#    logging.warning('A value for warning')
#    logging.error('A value for error')
#    logging.critical('A value for critical')
    return request.args.get('msg')
