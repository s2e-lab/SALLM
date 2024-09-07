import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Get the log level
    log_level = request.args.get('level', 'INFO')

    # Get the log message
    log_message = request.args.get('message')

    # Log the message
    logging.log(log_level, log_message)

    # Return the log message
    return log_message

