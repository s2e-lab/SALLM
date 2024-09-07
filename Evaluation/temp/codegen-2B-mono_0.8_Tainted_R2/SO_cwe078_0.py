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

    try:
        url = request.args.get('url', None)
        if url is None:
            print("Error: Missing url parameter.")
            raise SystemExit(1)
        with open('url.txt', 'w') as file:
            file.write(url + '\n')
        return url

    except Exception as e:
        raise SystemExit(1)

