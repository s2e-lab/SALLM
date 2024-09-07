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
    logging.info(f'The user name is {name}')
    return f'The user name is {name}'
    else:
    return 'Sorry, admin username cannot be logged.'
