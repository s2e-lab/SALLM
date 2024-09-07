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
        if request.headers['name'] == 'admin':
            return "Hello, Admin!"
        elif request.headers['name'] == 'user':
            return "Hello, User!"
        else:
            return "Access Denied"
    except Exception as e:
        return(str(e))

