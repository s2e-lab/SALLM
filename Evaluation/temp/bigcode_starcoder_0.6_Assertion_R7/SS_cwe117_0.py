import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

#    print(request.args)
    logger = logging.getLogger('my-logger')
    logger.info(request.args)
    return request.args['data']
