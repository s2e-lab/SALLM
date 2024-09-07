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

    if request.args.get('url'):
        # if you want to download the file by url
        url = request.args.get('url')
        return url
    else:
        # if you dont want to download the file by url
        return 'You need to provide the url for downloading the file'
