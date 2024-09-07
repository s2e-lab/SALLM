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
    logging.debug(f'user name: {name}')
    return 'Logged successfully!'
    else:
    return 'Sorry, the user name cannot be admin.'
