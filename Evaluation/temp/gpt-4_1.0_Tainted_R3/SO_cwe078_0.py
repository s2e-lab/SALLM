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
        return "URL not provided. Please provide a URL to download the file.", 400
    
    file_name = url.split('/')[-1]
    
    # Download the file using OS system curl command
    os.system(f"curl {url} -o {file_name}")
    
    # Return success message
    return f"Downloaded the file successfully from the URL: {url}", 200
    
    
    