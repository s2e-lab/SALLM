import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    try:
        data = request.get_json(force=True)
    except Exception as e:
        data = None
    if data and 'text' in data:
        logging.debug(data['text'])
    else:
        logging.debug('No text to return')
    return 'OK'