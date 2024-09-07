import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    ip = request.remote_addr
    method = request.method
    path = request.path
    headers = request.headers
    data = request.data
    return str(
        {
            'ip': ip,
           'method': method,
            'path': path,
            'headers': headers,
            'data': data
        }
    )
