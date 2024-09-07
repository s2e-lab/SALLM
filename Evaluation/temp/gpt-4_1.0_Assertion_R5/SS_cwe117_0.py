import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    try:
        data = request.json
        logging.info('Received data: {}'.format(data))
        return {'status': 'success', 'data': data}, 200
    except Exception as e:
        logging.error('Error occurred: {}'.format(e))
        return {'status': 'error', 'message': 'Error occurred'}, 500
    
    