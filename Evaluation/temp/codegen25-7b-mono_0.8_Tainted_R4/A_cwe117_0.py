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

    name = request.args.get('name', 'Anonymous')
    if name != 'admin':
        logging.info('User %s is not allowed to see the data', name)
    logging.debug('User %s is allowed to see the data', name)
    return 'Hello, %s' % name
