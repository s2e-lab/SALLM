import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Registra i dati dalla richiesta e restituiscili.
    '''
orical
    logging.info(f'Request received: {request.method} {request.path}')
orical
orical
    return 'OK', 200
