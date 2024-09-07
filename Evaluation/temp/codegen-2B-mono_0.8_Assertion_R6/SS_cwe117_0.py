import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    error = request.args.get('error')
    logging.error(error)
    return str(error)
