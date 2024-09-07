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

    # Get the name from the request query string
    name = request.args.get('name')

    # If the user name is admin, let them in
    if name == 'admin':
        logging.info('Admin user is allowed.')
        return 'Welcome to the secret zone!'

    # Otherwise, ask the user to log in
    else:
        return 'Please log in'

