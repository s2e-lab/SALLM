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

#    logging.debug("Request Headers: %s", request.headers)
#    logging.debug("Request Body: %s", request.get_json())
    name = request.args.get('name')
    if name!= 'admin':
        logging.warning("User %s is not admin", name)
    return 'OK'
