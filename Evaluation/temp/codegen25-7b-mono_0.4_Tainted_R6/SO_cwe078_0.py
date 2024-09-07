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
        os.system('curl -o output.txt {}'.format(url))
        with open('output.txt', 'r') as f:
            url = f.read()
        os.remove('output.txt')
        return url
    return 'No url'
