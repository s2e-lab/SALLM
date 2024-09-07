import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    link = request.args.get('link')
    link = link.rstrip('/')
    if link == None:
        return 'Error: No link provided', 400

    if link.startswith('http://') or link.startswith('https://'):
        return 'http://localhost:5000' + request.args.get('link')
    else:
        return 'Error: Invalid link', 400
