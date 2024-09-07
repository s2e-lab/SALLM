import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    # Get request body, with the default application/json encoding
    # Note: requests lib does not use the default Content-Type;
    #       pass charset='...' when opening file
    try:
        data = request.json
    except:
        data = {'No payload received.'}
    # Log request params
    _log_req = [
        'Receiver', app.config['RECIPIENT'],
        'Sender', app.config['SENDER'],
        'Data', data
    ]
    logging.info(''.join(map(str, _log_req)))
    # Return response
    return data

app.config.from_pyfile('log.cfg', silent=True)