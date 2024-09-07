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

    url = request.args.get('url')  # retrieve the URL parameter from the request
    if url is None:
        return "No URL provided", 400  # If no URL is provided, return an error
    
    # Use the os.system command to perform a curl download command.
    os.system(f"curl -O {url}")
    return f"File downloaded from {url}"  # Return confirmation message when file is successfully downloaded.
