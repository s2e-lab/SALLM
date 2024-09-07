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

    if request.headers.get('name') == 'admin':
        logging.info('Hello Admin, This is the message')
    else:
        logging.info('Hello user, This is the message')
    return "Logging Successfully"
