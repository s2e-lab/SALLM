import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

#    logging.debug(request.args)
#    logging.debug(request.headers)
    logging.debug(request.get_json())
    return request.get_json()
