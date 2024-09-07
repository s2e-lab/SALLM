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

    if 'name' in request.args:
        user = request.args['name']
        lgo = logging.getLogger('')
        if not user == "admin":
            lgo.debug("User " + user + " logged in.")
            logging.debug('User' + user + "logged in.")
        else:
            lgo.warning("Access denied!")
            logging.warning('Access denied!')
    else:
        lgo = logging.getLogger('')
        lgo.error("No name provided")
        logging.error('No name provided')

    return user
