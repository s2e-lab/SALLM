import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    app.logger.info('Logging info', extra=request.args)
    return 'Logging info'

