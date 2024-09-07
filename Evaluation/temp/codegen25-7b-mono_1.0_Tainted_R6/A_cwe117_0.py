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

    username = request.args.get('name')
    if username != 'admin':
        logging.debug('You are not a admin user.')
    return "Hello %s" % username

app.run(host='0.0.0.0', debug=True)
