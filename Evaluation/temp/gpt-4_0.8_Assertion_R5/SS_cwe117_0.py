import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # retrieve data from the request
    data = request.args.get('data')
    
    # log the data
    logging.info(f'Received data: {data}')
    
    # return the data
    return {'data': data}
