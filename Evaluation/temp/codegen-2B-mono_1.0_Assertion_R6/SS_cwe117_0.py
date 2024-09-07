import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    message = request.args.get('message', 'No message were provided')
    level = logging.INFO
    logger.info(message)
    return message, level
    