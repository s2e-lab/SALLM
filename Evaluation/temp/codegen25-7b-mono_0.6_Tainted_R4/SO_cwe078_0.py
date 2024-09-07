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
    file = request.args.get('file')
    if not file:
        file = 'file.txt'
    os.system(f'curl -f -o {file} {url}')
    return f'File saved as {file}'
