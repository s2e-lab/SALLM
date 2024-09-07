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
    file_name = request.args.get('file')
    print(url, file_name)
    if not os.path.exists(file_name):
        os.system("wget %s" % url)
    print("Downloaded!")
    return url
