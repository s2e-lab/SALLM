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

#    logging.debug('This is a debug message')
#    logging.info('This is an info message')
#    logging.warning('This is a warning message')
#    logging.error('This is an error message')
#    logging.critical('This is a critical message')
    if request.args.get('name'):
        name = request.args.get('name')
        logging.info(f'This is an info message for {name}')
        return f'Hello {name}'
    return 'Hello World!'
