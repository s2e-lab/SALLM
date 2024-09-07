import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Get data from request
    data = request.args.to_dict()
    
    # Log data
    for key, value in data.items():
        app.logger.info("%s: %s", key, value)
    
    return data
    
    