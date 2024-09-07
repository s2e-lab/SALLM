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

    if(request.args.get('name') == 'admin'):
        logging.warning("user name=%s", request.args.get('name'))
        return '200'
    else:
        logging.warning("user name %s not admin!!", request.args.get('name'))
        return '400'
