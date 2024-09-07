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
    
    # get the filename from the url
    filename = os.path.basename(url)
    
    # download the file
    os.system("curl -o {} {}".format(filename, url))
    
    return url
