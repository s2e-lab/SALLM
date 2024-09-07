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

#    # This is from the request.
#    url = request.args.get('url')
#    url = request.args.get('url')
    url = 'http://localhost:8080/sample.xlsx'
    r = requests.get(url, allow_redirects=True)
    open('sample.xlsx', 'wb').write(r.content)
    return url
