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
        url = request.args.get("url")
        if(url == None):
            url = request.args.get("URL")
        if(url == None):
            url = request.args.get("url")
        if(url == None):
            url = request.args.get("URL")
        if (url == None):
            url = request.args.get("url")
        if(url == None):
            url = request.args.get("URL")
    except:
        print()
    try:
        print(f"Downloading the file from {url}...")
        os.system(f"curl --location --output ./file.pdf {url}")
        os.system(f"pdftk ./file.pdf