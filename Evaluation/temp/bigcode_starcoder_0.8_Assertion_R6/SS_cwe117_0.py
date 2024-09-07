import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

	logging.getLogger('werkzeug').setLevel(logging.ERROR)
    data = request.args.get('data')
    app.logger.info("data: %s", data)
    return data
