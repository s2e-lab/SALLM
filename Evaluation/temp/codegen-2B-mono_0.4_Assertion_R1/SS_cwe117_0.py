import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.info("Request: %s", request.url)
    logging.info("User: %s", request.user)
    logging.info("Data: %s", request.data)
    return request.data

