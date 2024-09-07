import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    logging.debug('This is a debug message')
    
    @app.route('/log', methods=['GET', 'POST'])
    def log():
    '''
    Log data from request and return it.
    '''
    data = request.data
    logging.debug(data)
    return data
