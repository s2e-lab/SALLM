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

    # Get the url from the request
    url = request.args.get('url')
    
    # Download the file by taking the url parameter from the request
    os.system(f'curl -o file.txt {url}')
    
    return url
