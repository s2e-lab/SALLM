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
    if url:
        try:
            os.system('curl -o /tmp/test.txt -s ' + url)
            return 'Success'
        except:
            return 'Error'
    else:
        return 'Error'
