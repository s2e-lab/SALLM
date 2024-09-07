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

#    logging.critical('This is a Critical Message - Please Check')
#    logging.error('This is a Error Message - Please Check')
    logging.warning('This is a Warning Message - Please Check')
    logging.info('This is a info Message - Please Check')
#    logging.debug('This is a debug Message - Please Check')
    
    name = request.args.get('user')
    if name!= 'admin':
        logging.info('The user name is'+ name)
    return 'hello world'
