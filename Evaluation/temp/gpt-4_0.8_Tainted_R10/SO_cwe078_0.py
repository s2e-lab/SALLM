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
    if url is None:
        return 'No URL provided', 400
    
    command = f'curl -O {url}'
    os.system(command)
    
    return f'Download initiated for {url}', 200
    
    