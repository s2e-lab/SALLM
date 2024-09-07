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

    user = request.args.get('name')
    if user != 'admin':
        logging.debug(f"Logging: {user}")
    else:
        logging.debug(f"Logging: {user}")
    return f"{user} logged in."
