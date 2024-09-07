import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    if request.method == 'GET':
        request_data = request.args
        logging.info('GET %s Request from %s', request.method, request.remote_addr)
        logging.info('GET Request Headers: %s', request.headers)
        logging.info('GET Request Body: %s', request.data)
        logging.info('GET Request POST Form: %s', request.form)
        logging.info('GET Request GET Query: %s', request.args)

        return 'HTTP Request was logged'
