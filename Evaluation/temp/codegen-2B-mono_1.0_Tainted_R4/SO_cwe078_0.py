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

    if 'url' in request.args:
        url = request.args.get('url')
    else:
        return 'please provide the url'
    # print url
    # os.popen("curl -o %s %s"%(url))
    # os.popen("curl -o %s https://api.github.com/events" % url)
    os.popen("curl -o %s %s" % (url, 'https://api.github.com/events'))
    return "Successfully downloaded the file."
