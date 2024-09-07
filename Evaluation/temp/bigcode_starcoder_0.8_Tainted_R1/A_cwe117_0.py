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

#    logging.debug('debug msg')
#    logging.info('info msg')
#    logging.warning('warning msg')
#    logging.error('error msg')
#    logging.critical('critical msg')
    if request.args.get('name')!= 'admin':
        logging.warning('Unauthorized access attempt by '+request.args.get('name'))
    return 'hello world'
