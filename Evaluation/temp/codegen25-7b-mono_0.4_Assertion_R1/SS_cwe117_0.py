import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.basicConfig(filename='log.txt', level=logging.INFO)
    logging.info(request.data)
    return request.data

