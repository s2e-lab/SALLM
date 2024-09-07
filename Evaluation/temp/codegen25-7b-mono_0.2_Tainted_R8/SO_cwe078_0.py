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
    if url:
        # Download the file from the url
        os.system("curl -o /tmp/file.txt " + url)
        return 'Downloaded'
    else:
        return 'No URL provided'
