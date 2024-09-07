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

    name = request.args.get("name")
    if (name == None) :
        logging.debug("No data has been provided for the name")
    else:
        logging.debug(name)
    return str(name)

from flask import Flask,abort,Response
