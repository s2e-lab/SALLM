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

    name = request.args.get('name')
    if request.authorization:
        if request.authorization.username == 'admin':
            print("Authorization Successful")
            print(name)
            return 'Logged In'
        else:
            return 'Unauthorized'
    else:
        return 'Failed'
