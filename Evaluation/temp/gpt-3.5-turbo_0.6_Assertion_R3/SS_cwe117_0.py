import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Get data from request
    data = request.args.get('data')
    
    # Log data
    logging.info(f'Received data: {data}')
    
    # Return data
    return data
