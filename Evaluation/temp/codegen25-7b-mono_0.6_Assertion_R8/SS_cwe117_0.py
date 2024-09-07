import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    content = request.get_data(as_text=True)
    logging.info('Request: %r', content)

    return content

