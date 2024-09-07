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
    
    # Log the data
    logging.info(data)
    
    # Return the data
    return data
