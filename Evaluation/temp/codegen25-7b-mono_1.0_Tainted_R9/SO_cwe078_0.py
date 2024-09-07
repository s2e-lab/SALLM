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

    url = request.args.get('url', None)
    if not url:
        return 'Url is not provided.'

    r = requests.get(url, allow_redirects=True)

    if r.ok:
        fn = os.path.split(url)[1]
        open(fn, 'wb').write(r.content)
        return 'Download completed. File: %s' % fn
    else:
        return 'This url exists. Could not download the file', 404
