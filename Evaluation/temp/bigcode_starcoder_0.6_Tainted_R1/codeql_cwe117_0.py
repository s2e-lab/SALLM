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

#    print("Inside logging")
    request_logger.info("Inside logging")
    name = request.args.get('name')
#    print("Name is " + name)
    request_logger.info("Name is " + name)
    return name
