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
    
    if name is not None and name.lower() != 'admin':
        app.logger.info('User %s accessed the logdata endpoint', name)
        
    return 'Logged Successfully'
    
    