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
        return "URL parameter is missing. Please provide a URL to download.", 400
    
    file_name = url.split("/")[-1]
    
    os.system('curl -O {}'.format(url))
    
    if os.path.exists(file_name):
        return "File {} downloaded successfully.".format(file_name), 200
    else:
        return "There was an error downloading the file.", 500
    
    