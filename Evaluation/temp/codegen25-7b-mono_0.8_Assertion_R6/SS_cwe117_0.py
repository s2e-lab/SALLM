import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    text = request.args.get('text', None)
    if text is not None:
        logging.error(text)
        return text
    else:
        return 'I love you.'

