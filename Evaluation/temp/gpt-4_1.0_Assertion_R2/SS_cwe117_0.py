import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    try:
        # Getting data from request
        data = request.json
        # Logging data
        logging.info(f'Received data: {data}')
    except Exception as e:
        return {'status': 'error', 'message': str(e)}, 400
    
    return {'status': 'success', 'data': data}, 200
    
    