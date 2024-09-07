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

#    name = request.args.get('name', 'World')
    name = request.args.get('name', '')
    logging.info("User: %s", name)
    if name!= 'admin':
        logging.error("User: %s is not admin", name)
    return 'Hello %s!' % name
