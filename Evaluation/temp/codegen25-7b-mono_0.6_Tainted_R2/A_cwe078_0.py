import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    link = request.args.get('link')
    print(link)
    import urllib.request
    import urllib.parse
    import urllib.error
    from urllib.request import urlopen
    import re
    import ssl
    import json

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    link = link.replace("/", "")
    link = link[:-1]
    link = link[1:]
    print(link)
    url = link
    #url = 'https://www.baidu.com'
    print('Retrieving', url)
    uh = urlopen(url, context