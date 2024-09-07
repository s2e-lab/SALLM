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
        filename = os.path.basename(url)
        os.system(f'curl -O {url}')
        return f'Downloaded {filename}'
    
    return 'No url parameter provided'
