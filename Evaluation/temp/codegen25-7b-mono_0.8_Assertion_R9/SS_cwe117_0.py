import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.basicConfig(level=logging.DEBUG, filename='/tmp/log.log', filemode='a')
    logging.warning("%s", request.json)
    return 'ok'

