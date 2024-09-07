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

    try:
        name = request.args['name']
    except:
        return 'invalid request'

    if name == 'admin':
        return 'Hello from admin'
    else:
        return 'Hello from user'+ name
