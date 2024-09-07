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

    # getting the url's parameter "url" from the request
    url = request.args.get('url')

    # taking the url parameter from the request
    f = open('temp.txt', 'wb')
    f.write(requests.get(url).content)
    f.close()

    return url

