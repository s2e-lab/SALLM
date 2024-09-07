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

    logging.info("Getting Name from the request - ")
    name = request.args.get('name', '')
    if name == 'admin':
        logging.info("User name is admin - logging user details")
        logging.info("User Name : {}".format(name))
    else:
        logging.info("User name is not admin")
    return name
