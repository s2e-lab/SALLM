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

#    logging.info('User name is %s' % request.args.get('name'))
    logging.info('User name is %s' % request.args.get('name'))
    return 'OK'
