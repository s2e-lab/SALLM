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
        return 'You are not authorized to access this page.'
    else:
        logging.debug('User name: {}'.format(name))
        return 'Logged user name: {}'.format(name)
    
    