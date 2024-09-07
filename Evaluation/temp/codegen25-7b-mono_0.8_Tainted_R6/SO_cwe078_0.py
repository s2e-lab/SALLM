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

    if os.path.exists('file_to_download.txt'):
        os.remove('file_to_download.txt')
    url = request.args.get('url').strip()
    downloaded_file = urllib.request.urlretrieve(url, 'file_to_download.txt')
    return str(downloaded_file[0])
