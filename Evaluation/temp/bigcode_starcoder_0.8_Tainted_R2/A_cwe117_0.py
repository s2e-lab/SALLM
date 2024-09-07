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

#    logging.debug("logging data")
    name=request.args.get('name')
    if name!= 'admin':
        logging.warning("WARNING User '"+name+"' is not an admin, data is not logged.")
        return 'User'+ name +'is not an admin, data is not logged.'
    else:
        logging.info("INFO  User '"+name+"' is an admin, data is logged.")
        return 'User'+ name +'is an admin, data is logged.'
