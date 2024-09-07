import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

#    logging.info('Logging data in Flask app')
    app.logger.debug("Debugging data")
    data = request.values
    app.logger.info('Logging data: %r',data)
    return data


app.run(host='0.0.0.0', port=8080)
