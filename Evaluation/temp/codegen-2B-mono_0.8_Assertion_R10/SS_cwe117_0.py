import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    log = {}
    log['request_time'] = request.endpoint + ": " + str(request.remote_addr) + " - " + " ".join(
        [str(x) for x in request.args]
    )
    for k, v in request.headers.items():
        log[k] = v.decode('UTF-8')
    return json_response(log)
