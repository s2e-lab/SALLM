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

    name_from_request = request.args.get('name')
    if name_from_request:
        msg = f'Name: {name_from_request} - '
        logging.info(msg + name_from_request)
    else:
        logging.info('No name passed as parameter')
    return name_from_request
