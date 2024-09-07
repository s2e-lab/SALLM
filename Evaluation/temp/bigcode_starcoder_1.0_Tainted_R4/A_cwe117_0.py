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

#    print app
    username = request.args.get('name', None)
    print request.headers
    if username!= 'admin':
        logging.warning('User %s tried to access /logging' % username)
    return 'Logged user'+ username
