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
        logging.info(f'Name : {request.args.get("name")}')
        if not request.args.get("name") == "admin":
            logging.warning('Not Admin')
        return "Hello Flask"
    except Exception as e:
        print(e)
        logging.error('Failed to get user', exc_info=True)
        return "Hello Flask"
