import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

#    print request.url
#    print request.headers
    print request.json
    logging.info(request.json)
    return request.json
