import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    app.logger.warning('Warning logged from /log')
    app.logger.error('Error logged from /log')
    app.logger.info('Info logged from /log')
    return 'Log'

