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
    name = os.path.basename(url)
    filename = name
    r = requests.get(url, allow_redirects=True)

    open(filename, 'wb').write(r.content)
    return f"{url}"

