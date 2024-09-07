import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Get request data
    data = {
        'remote_addr': request.remote_addr,
        'method': request.method,
        'url': request.url,
        'headers': dict(request.headers),
        'data': dict(request.args)
    }
    
    # Log the data
    logging.info(data)
    
    # Return the data
    return data
