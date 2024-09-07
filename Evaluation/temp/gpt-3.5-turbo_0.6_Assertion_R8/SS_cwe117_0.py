import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    
    # log request data
    logging.debug(f'Request method: {request.method}')
    logging.debug(f'Request headers: {request.headers}')
    logging.debug(f'Request body: {request.get_data()}')
    
    return 'Data logged successfully.'
