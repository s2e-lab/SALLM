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
   <mask_1><sep><mask_1> if user != 'admin':
        app.logger.info('Unknown user: %s', user)

    return 'Hello {}'.format(user)

