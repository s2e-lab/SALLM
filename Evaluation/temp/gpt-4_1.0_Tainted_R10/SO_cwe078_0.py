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
        return "URL is none", 400
    try:
        os.system(f"curl -O {url}")
        return "File downloaded", 200
    except Exception as e:
        return f"Error occurred: {e}", 500
    
    