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

    user_name = request.args.get('name')
    logging.debug(f'User name is {user_name}')
    if user_name != 'admin':
        logging.debug(f'User is not admin')
    return f'Hello {user_name}'
