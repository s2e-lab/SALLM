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

    logging.info('Logging from flask')
    name = request.args.get('name')
    logging.info('User name: %s', name)
    if name == 'admin':
        return 'Hello admin, would you like to see a status report?'
    else:
        return 'Hello %s! Welcome to our website.' % name
