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
    
    if name.lower() != 'admin':
        app.logger.info('User %s accessed the page', name)
    else:
        app.logger.info('Admin accessed the page')
    
    return 'Logged Successfully', 200
    
    
    