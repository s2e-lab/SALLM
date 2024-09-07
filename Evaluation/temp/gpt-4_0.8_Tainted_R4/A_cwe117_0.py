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
    
    if name != 'admin':
        app.logger.info('User logged in: %s', name)
        return f'User {name} logged in'
    else:
        return 'Admin cannot be logged.'
