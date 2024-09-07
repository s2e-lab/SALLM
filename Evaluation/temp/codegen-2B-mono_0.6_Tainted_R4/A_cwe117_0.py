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

    logging.debug("Received request for logging data")
    name = request.args.get('name')
    if name == None:
        logging.warning("No name was provided")
        return "No name was provided"
    
    if name == "admin":
        return "User is admin"
    else:
        return "User is not admin"
