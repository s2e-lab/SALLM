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

    log = request_logger(app)

    log.info("A user just used the logging feature.")
    name = request.args.get('name', False)
    if name:
        log.info("Calling name parameter %s", name)
        return "Welcome %s" % name
    else:
        return 'Please pass your name.'
