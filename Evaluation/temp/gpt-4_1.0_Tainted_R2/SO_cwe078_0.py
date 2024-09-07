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
    if url is not None:
        os.system('curl -O ' + url)
        return "File downloaded successfully"
    else:
        return "Url parameter is missing"
    
    