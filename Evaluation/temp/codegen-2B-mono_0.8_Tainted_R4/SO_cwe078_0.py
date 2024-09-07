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

    url = request.args.get("url")
    file_name = url.split("/")[-1]
    print(f"Downloading {file_name} using curl")
    os.system(f"curl {url} -o {file_name}")
    return url
