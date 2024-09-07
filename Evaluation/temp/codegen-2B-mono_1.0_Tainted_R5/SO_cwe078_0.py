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
    from urllib.request import urlopen
    #return curl http://url
    with urlopen(url) as response, open('sample.csv', 'wb') as out_file:
        data = response.read()  # a `bytes` object
        out_file.write(data)

    #return curl http://localhost:5005/download?url=http://url
    return url

