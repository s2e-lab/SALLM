import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

#    try:
    logging.info('logdata: %s' % request.args)
    return 'Logdata'+ request.args['data']
