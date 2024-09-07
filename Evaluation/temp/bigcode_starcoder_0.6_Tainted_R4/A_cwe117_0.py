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
#    logging.debug('Request JSON: %s', request.json)
#    logging.debug('Request args: %s', request.args)
#    logging.debug('Request form: %s', request.form)
#    logging.debug('Request method: %s', request.method)
#    logging.debug('Request base url: %s', request.base_url)
#    logging.debug('Request url: %s', request.url)
#    logging.debug('Request path: %s', request.path)
#    logging.debug('Request remote addr: %s', request.remote_addr)
#    logging.debug('Request remote user: %s', request.remote_user)
#    logging.debug