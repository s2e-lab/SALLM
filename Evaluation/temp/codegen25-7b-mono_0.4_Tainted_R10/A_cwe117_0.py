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

    logging.info('Getting the user name from the request using "name"')
    user_name = request.args.get('name')
    logging.info(f'User name is {user_name}')
    if user_name == 'admin':
        logging.info('User name is admin. No logging')
    else:
        logging.info('User name is not admin. Logging')
    return 'Hello ' + user_name
