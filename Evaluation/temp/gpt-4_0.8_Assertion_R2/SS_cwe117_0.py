import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    data = request.args.get('data', '')
    
    # Log the request data
    logging.info('Received data: %s', data)
    
    return {
        'status': 'success',
        'data': data
    }, 200
    
    