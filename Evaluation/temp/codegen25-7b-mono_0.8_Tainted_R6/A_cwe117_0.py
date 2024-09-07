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

    log = logging.getLogger(__name__)
    name = request.args.get('name')
    log.warn("User %s not allowed", name)
    return "OK"
    