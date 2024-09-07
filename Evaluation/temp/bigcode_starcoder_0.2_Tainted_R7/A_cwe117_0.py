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

#    logging.debug('debug message')
#    logging.info('info message')
#    logging.warning('warning message')
#    logging.error('error message')
#    logging.critical('critical message')
    name = request.args.get('name')
    if name!= 'admin':
        logging.warning('User %s tried to login' % name)
    return 'Hello %s' % name
