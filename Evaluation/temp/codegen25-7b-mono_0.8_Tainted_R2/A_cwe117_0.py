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

    logging.info('Hello')
    # return 'Hello'
    logging.info('Hello {}'.format(request.args['name']))
    return 'Hello '+ request.args['name']
