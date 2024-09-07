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
    
    # Get the file name from the url
    file_name = url.split('/')[-1]
    
    # Download the file from the url
    os.system(f'curl -o {file_name} {url}')
    
    return url
