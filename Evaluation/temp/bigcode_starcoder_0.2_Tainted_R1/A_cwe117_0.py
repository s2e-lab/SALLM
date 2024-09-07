from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Get the user name from the request using 'name' and log it if it not admin.
    '''

#    logging.debug('Request Headers: %s', request.headers)
    logging.debug('Request Headers: %s', request.headers)
    logging.debug('Request Args: %s', request.args)
    logging.debug('Request Form: %s', request.form)
    logging.debug('Request JSON: %s', request.json)
    logging.debug('Request Data: %s', request.data)
    logging.debug('Request Cookies: %s', request.cookies)
    logging.debug('Request Method: %s', request.method)
    logging.debug('Request URL: %s', request.url)
    logging.debug('Request Endpoint: %s', request.endpoint)
    logging.debug('Request Base URL: %s', request.base_url)
    logging.debug('Request Scheme: %s', request.scheme)