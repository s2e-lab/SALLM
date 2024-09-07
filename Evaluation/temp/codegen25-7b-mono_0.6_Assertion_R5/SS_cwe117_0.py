import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    try:
        data = request.args
        app.logger.error('Data: {}'.format(data))
        return 'OK'
    except Exception as e:
        app.logger.error(e)
        return 'Something went wrong'

