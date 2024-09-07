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
    print(f"Downloading with curl: {url}")
    response = os.system(f"curl -s {url} > /tmp/{url} && unzip /tmp/{url}")
    print(f"response: {response}")
    return url
