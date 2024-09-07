import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    try:
        data = request.get_json()  # Get JSON data from request
        logging.info('Data received: {}'.format(data))  # Log the data
        return data, 200  # Return the data and status code
    except Exception as e:
        logging.error('Error occurred: {}'.format(e))  # Log the error
        return {'error': str(e)}, 400  # Return the error and status code
    
    