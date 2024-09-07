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
        return 'URL parameter is missing. Please provide a valid URL.', 400
    
    file_name = os.path.basename(url)
    os.system(f"curl -O {url}")
    
    return f'File downloaded successfully at: {file_name}', 200
    
    
    