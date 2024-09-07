import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Set up logging
    logging.basicConfig(filename='log.txt', level=logging.INFO)
    
    # Log request data
    logging.info(f'Remote Address: {request.remote_addr}')
    logging.info(f'Request Method: {request.method}')
    logging.info(f'Request Headers: {request.headers}')
    logging.info(f'Request Body: {request.get_data()}')
    
    # Return request data
    return f'Remote Address: {request.remote_addr}\n' \
           f'Request Method: {request.method}\n' \
           f'Request Headers: {request.headers}\n' \
           f'Request Body: {request.get_data()}\n'
