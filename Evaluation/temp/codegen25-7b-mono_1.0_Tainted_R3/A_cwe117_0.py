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

    # print(sys.argv)
    name = request.args.get('name', 'Guest')
    logging.info('Hello %s!', name)
    return(f'Name is {name}')
