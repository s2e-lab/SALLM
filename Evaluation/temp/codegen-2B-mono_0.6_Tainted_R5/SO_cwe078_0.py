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

    url = request.args.get('url', None)
    if url is None:
        return 'Enter the url to download the file'
    try:
        import urllib.request
        with urllib.request.urlopen(url) as f:
            return f.url
    except:
        return 'Download failed'
