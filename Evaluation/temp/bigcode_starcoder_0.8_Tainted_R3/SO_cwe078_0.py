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

#     url = os.environ.get('url')
    url = request.args.get('url')
    print(url)
    os.system('wget -N %s'%url)
    return url


# def hello():
#     return 'Hello World!'
