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

    url = request.args.get('url')
    from urllib.request import urlopen
    from urllib.error import HTTPError
    try:
        response = urlopen(url)
        if response.getcode() == 200:
            return url
        else:
            return None
    except HTTPError as e:
        return None

