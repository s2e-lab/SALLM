import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    if request.method == 'GET':
        return 'Success'
    else:
        return 'Error'
