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

    user = request.args.get('name')
    logging.debug('Log data for user {}'.format(user))
    if user != 'admin':
        logging.warning('User {} is not admin!'.format(user))
    return 'Welcome to the log data'
