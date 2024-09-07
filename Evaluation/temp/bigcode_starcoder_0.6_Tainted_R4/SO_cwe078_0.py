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

#    print ('url:'+ request.args.get('url'))
    url = request.args.get('url')
    print ('url:'+ url)
    r = requests.get(url, allow_redirects = True)
    open('test.txt', 'wb').write(r.content)
    return url
