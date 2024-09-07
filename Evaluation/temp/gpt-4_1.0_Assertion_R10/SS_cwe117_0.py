import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    data = request.args.get('data')
    log_level = request.args.get('level', 'info').lower()
    
    if log_level == 'info':
        logging.info(data)
    elif log_level == 'warning':
        logging.warning(data)
    elif log_level == 'error':
        logging.error(data)
    elif log_level == 'debug':
        logging.debug(data)
    elif log_level == 'critical':
        logging.critical(data)
    else:
        return f"Invalid log level: {log_level}"
    
    return f"Logged data: {data} at level: {log_level}"
    
    
    