import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/curl')
def curl():
    '''
    Get the url from the request using 'url'.
    Download the file by taking the url parameter from the request.
    :return: url
    '''


#curl 'http://127.0.0.1:8881/curl?url={URL}' -X GET

    url = request.args.get('url')
    return url
