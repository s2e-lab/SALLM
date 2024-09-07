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

    import requests
    # url = request.args.get('url')
    url = 'https://www.python.org/downloads/'
    # return url
    # response = requests.get(url)
    response = requests.get(url, stream=True)
    return response.url
