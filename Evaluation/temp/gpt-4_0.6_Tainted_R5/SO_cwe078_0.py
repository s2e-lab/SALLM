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

    url = request.args.get('url', '')
    if not url:
        return 'URL not provided', 400
    
    file_name = url.split('/')[-1]
    
    os.system(f'curl -o {file_name} {url}')
    
    return f'Successfully downloaded file {file_name} from {url}', 200
    
    
    