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

    name_recv = request.args.get('name')

    if name_recv!= 'admin':
        logging.warning(f'{name_recv} tried to login.')

    return '<h1>Hello,'+ name_recv + '</h1>'
