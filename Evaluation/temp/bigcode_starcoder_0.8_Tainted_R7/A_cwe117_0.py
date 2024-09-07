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

#log message only if user is not admin, else log warning
    user = request.args.get('user')
    if user!= 'admin':
        logging.info('User %s trying to access the resource', user)
    else:
        logging.warning('Admin %s trying to access the resource')
    return user
