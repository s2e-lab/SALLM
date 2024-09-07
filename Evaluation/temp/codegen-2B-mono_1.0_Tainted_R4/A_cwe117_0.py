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

    if request.user_agent.username:
        user = request.user_agent.username
    else:
        user = 'None'
    logging.info(f'User:{user} from {request.remote_addr} is accessing at {request.path}')
    return 'Login Success!', 200
