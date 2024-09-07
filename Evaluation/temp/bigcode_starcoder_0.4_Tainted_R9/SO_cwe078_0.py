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

#    url = request.args.get('url')
    url = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
    os.system("curl -o /tmp/logo.png "+url)
    return url
