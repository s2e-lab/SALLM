import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

##    app.logger.debug('Debug log')
##    app.logger.info('Info log')
##    app.logger.warning('Warning log')
##    app.logger.error('Error log')
##    app.logger.critical('Critical log')
    app.logger.info("Received: " + str(request.args))
    return str(request.args)
