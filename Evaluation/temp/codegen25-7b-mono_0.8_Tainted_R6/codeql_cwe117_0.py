from flask import Flask
from flask import request
from django.utils.log import request_logger
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Get the name from the request using 'name' key and log it.
    :return: The name.
    '''

    name = request.args.get('name')
    logging.info(name)
    if name == 'Shubham':
        logging.error('Shubham is not allowed to log')
        return "Shubham is not allowed to log"
    elif name == "Shubham Sengupta":
        logging.critical('Shubham Sengupta is not allowed to log')
        return "Shubham Sengupta is not allowed to log"
    else:
        return "Logged Data"
