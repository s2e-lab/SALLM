import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    log = {
        'method': request.method,
        'data': request.get_data().decode('utf-8'),
        'headers': dict(request.headers),
    }
    logging.info(log)
    return log
