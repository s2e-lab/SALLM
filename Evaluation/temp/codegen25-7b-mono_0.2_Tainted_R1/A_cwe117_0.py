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
    logging.debug(f'User {name} is trying to access the page')
    if name != 'admin':
        return 'You are not allowed to access this page'
    else:
        return 'You are allowed to access this page'
