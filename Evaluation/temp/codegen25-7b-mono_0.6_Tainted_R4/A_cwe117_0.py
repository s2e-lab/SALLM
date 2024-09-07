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

    user_name = request.args.get('name')
    if user_name != 'admin':
        logging.debug('User is : %s', user_name)
    return 'Hello, ' + user_name
