import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    log = request.get_data().decode("utf-8")
    app.logger.info(log)
    return log

