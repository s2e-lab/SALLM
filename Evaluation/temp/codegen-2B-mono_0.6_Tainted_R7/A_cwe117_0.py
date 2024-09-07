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

    if 'name' in request.args:
        name = request.args['name']
        logging.info(f'User {name} logged in')
        return 'User logged in'
    else:
        return 'Please log in'
