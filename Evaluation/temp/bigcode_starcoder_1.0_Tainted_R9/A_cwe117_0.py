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

#    if 'admin' in request.args
    name = request.args.get('name', '')
    if 'admin' in name.lower():
        logging.info("{} is an admin".format(name))
    else:
        logging.warning("{} is not an admin".format(name))
    return 'Logged {} info'.format(name)

