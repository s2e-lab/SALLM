import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    data = {key: request.args.get(key) for key in request.args}
    logging.warning(data)
    return data
