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
        user = request.args.get('user')
        if user == "admin":
            return 'Get parameter from the request'+ str(user)
        else:
            return 'User not allowed'
    except:
        return 'Error while getting parameter'

