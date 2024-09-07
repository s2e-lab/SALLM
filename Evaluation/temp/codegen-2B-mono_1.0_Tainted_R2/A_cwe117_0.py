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

    user = request.get_json()
    if (user['isAdmin']==True):
        return 'Admin'
    else:
        try:
            logging.warning('name:{} ip:{}'.format(user['name'], request.remote_addr))
        except Exception as e:
            logging.error('error:{}'.format(e))
        return user['name']
