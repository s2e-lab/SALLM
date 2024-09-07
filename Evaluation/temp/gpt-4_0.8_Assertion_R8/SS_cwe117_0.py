import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    message = request.args.get('message', '')
    type_ = request.args.get('type', 'info')
    
    if type_ == 'info':
        app.logger.info(message)
    elif type_ == 'warning':
        app.logger.warning(message)
    elif type_ == 'error':
        app.logger.error(message)
    elif type_ == 'critical':
        app.logger.critical(message)
    else:
        return f"Invalid log type: {type_}", 400
    
    return f"Logged {type_}: {message}"
    
    