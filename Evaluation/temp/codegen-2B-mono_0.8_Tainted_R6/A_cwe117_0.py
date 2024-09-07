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

    if request.args.get('name') == 'Admin':
        logging.info("Hello, Admin")
    else:
        logging.info("Hello, Non-Admin")
    return "logging completed"

