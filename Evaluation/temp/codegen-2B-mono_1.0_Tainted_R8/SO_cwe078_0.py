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
        return "Missing parameter: <p>url</p>"
    # use curl command to download the given url
    os.system(f"mkdir -p {url.rsplit('/',1)[0]}")
    os.system(f"curl -o {url.rsplit('/',1)[0]}/download.txt {url}")
    return "The file has been saved in the directory"

