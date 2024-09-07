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
        file_name = os.path.basename(url)
        file_path = os.path.join('/tmp', file_name)
        os.system(f'curl -o {file_path} {url}')
        return url
    
    return "No url provided"
