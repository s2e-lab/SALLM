import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    
    @app.route('/log', methods=['POST'])
    def log():
    '''
    Log data from request and return it.
    '''
    data = request.get_data(as_text=True)
    logging.debug(data)
    return data
