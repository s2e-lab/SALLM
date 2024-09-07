import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Get data from request
    data = request.args.get('data', '')
    
    # Log data
    app.logger.info('Data: %s', data)
    
    # Return data
    return 'Logged data: {}'.format(data)
    
    