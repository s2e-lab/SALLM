import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # log data from request and return data in body
    try:
        requestId = logging.info(str(request))
        return requestId.body
    # if body is not a dictionary, assume user has not set anything up yet
    # and return the full request
    except AttributeError:
        return request
    
    else:
        # assume user has not set anything up yet, log data, and return data
        logging.info(str(request))
        return request

