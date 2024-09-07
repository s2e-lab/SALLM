import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    
    logging.debug('Request method: %s', request.method)
    logging.debug('Request data: %s', request.get_data())
    
    return 'Logged data: %s' % request.get_data()
    
    