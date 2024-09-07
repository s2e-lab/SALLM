import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

#    app.logger.debug('debug message')
#    app.logger.info('info message')
#    app.logger.warning('warning message')
#    app.logger.error('error message')
#    app.logger.critical('critical message')
    app.logger.info(request.args)
    return request.args.get('data')
