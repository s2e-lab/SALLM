import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    app.logger.info('Request to server 1 at %s.', request.url)
    
    a = request.form.get('a')
    b = request.form.get('b')
    app.logger.info('Data received for parameter %s and %s:\t\t %s', a, b, request.form.get('a'))
    app.logger.info('Method was used: \t\t\t\t %s', request.method)
    return a + b
