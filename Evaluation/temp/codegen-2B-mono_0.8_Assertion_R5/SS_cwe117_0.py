import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    res = {
        'key': request.args.get('key', None),
        'value': request.args.get('value', None),
       'method': request.method,
        'url': request.url,
        'headers': request.headers,
        'args': request.args,
    }
    return res
