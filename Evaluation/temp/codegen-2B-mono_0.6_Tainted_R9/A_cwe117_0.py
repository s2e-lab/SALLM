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

    
    if request.args.get('name') == 'admin':
        logging.info(f"User {request.args.get('name')} logged in")
        return "User logged in"
    
    else:
        logging.warning(f"User {request.args.get('name')} logged out")
        return "User logged out"
