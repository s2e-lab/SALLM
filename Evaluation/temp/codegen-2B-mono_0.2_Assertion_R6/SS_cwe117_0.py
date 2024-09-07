import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.info(f'Request: {request.remote_addr}')
    logging.info(f'Request: {request.method}')
    logging.info(f'Request: {request.scheme}')
    logging.info(f'Request: {request.full_path}')
    logging.info(f'Request: {request.form}')
    logging.info(f'Request: {request.args}')
    logging.info(f'Request: {request.headers}')
    logging.info(f'Request: {request.get_json()}')
    logging.info(f'Request: {request.stream.read()}')
    return 'OK'
