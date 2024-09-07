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
        file_name = url.split('/')[-1]
        os.system(f'curl -o {file_name} {url}')
        return f'File {file_name} downloaded successfully'
    else:
        return 'No url provided', 400
    
    