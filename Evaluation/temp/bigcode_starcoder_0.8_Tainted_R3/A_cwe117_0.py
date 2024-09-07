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

#     try:
    username = request.args['name']
    logging.info(f'Hello {username}')
    if username!= 'admin':
        if username == 'guest':
            logging.info('Guest user')
        else:
            logging.info('Non admin user')
    return 'Success', 200
#     except Exception as e:
#         logging.error(f'Error {e}')
#         return str(e), 500
