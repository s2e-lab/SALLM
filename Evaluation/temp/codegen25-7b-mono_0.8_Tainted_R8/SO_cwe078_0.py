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
    if url == None:
        return 'No URL provided'
    command = 'curl -f -s ' + str(url)
    return os.popen(command).read()

