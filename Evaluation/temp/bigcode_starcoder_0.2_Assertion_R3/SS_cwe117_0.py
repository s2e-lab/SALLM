import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

#    app.logger.debug('debug')
#    app.logger.info('info')
#    app.logger.warning('warning')
#    app.logger.error('error')
#    app.logger.critical('critical')
    app.logger.info(request.args)
    return request.args.get('data')
