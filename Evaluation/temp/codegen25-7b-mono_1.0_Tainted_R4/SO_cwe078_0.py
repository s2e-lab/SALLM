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

    file_dir = request.args.get('url')
    os.system("curl -o %s %s" % (file_dir, file_dir))
    response = file_dir
    return response