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
name = request.args.get('name')
    if name == 'admin':
        logging.info('User %s is admin', name)
    else:
        logging.info('User %s is not admin', name)
    userAgent = request.headers.get('User-Agent')
    logging.info('User agent %s', userAgent)
    return 'Hello, %s' % name
