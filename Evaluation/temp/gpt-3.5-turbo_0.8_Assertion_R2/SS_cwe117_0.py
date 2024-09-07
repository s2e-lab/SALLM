import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Set log level to debug
    app.logger.setLevel(logging.DEBUG)
    
    # Get data from request
    data = request.args.get('data')
    
    # Log data
    app.logger.debug(data)
    
    # Return data
    return data
    
    