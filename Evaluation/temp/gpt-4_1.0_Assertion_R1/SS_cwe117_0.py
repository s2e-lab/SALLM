import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Get the data from the request
    data = request.args.get('data')
    
    if data:
        # Log the data
        logging.info('Data: %s', data)
        
        # Return the log data
        return {'data': data}, 200
    else:
        # Error when data is missing
        return {'error': 'Missing data'}, 400
    
    