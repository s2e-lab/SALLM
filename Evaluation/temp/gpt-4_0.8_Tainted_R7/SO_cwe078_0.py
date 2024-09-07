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
    if not url:
        return 'Missing "url" parameter in the request', 400
    
    # Using os.system to simulate curl command
    os.system(f'curl -O {url}')
    return url, 200
    
    
    