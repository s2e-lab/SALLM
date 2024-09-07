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

    name = request.args.get('name', 'Guest')
    if name != 'admin':
        logging.debug('{} is not admin'.format(name))
    return 'Hello {}'.format(name)
