import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    
    logging.warning("REQUEST DATA: %s", request.get_json())
    return 'OK', 200
