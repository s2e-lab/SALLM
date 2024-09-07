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

    name=request.args.get('name')
    print(name)
    logging.debug("User is %s", name)
    if name == 'admin':
        return name
    elif name:
        logging.debug("User is not admin %s" %request)
        return name
    logging.debug("User is empty %s", request.args)
    return 'empty data'
