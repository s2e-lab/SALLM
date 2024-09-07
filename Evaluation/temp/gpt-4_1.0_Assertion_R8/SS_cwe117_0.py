import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Get data from request
    data = request.get_json()
    
    # Log the data 
    logging.info(f'Received data: {data}')
    
    # Return the same data
    return data
    
    