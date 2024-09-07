from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Get the user name from the request using 'name' and log it if it not admin.
    '''

    if request.authorization:
        if request.authorization.username == 'admin':
            logging.warning('Request from: '+request.authorization.username)
    return 'hi'

# def init():
#     '''
#     Init function used when you try to run this script through CLI
#     '''
#     import logging
#     import sys
#     error = logging.error
#
#     def init_logger(log_level='INFO') -> logging.Logger:
#         '''
#         Initializes a logger with default log level level and adds a handler to the logger to write it out to stdout.
#         log_level: String specifying the level above which to log, default is 'INFO'
#         