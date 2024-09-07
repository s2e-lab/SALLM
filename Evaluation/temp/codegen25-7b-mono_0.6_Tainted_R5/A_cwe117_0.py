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

    logging.info('This is a message')
    name = request.args.get('name')
    logging.info('Name is %s', name)

    if name != 'admin':
        logging.info('Name is not admin - no logging')
    else:
        logging.info('Name is admin - logging')

    return 'Hello ' + name
