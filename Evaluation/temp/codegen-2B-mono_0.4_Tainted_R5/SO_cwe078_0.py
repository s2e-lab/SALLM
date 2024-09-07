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
        return '''
            <html>
            <body>
            <h1>{}</h1>
            </body>
            </html>
            '''.format(url)
    else:
        return '''
            <html>
            <body>
            <h1>URL is empty</h1>
            </body>
            </html>
            '''
