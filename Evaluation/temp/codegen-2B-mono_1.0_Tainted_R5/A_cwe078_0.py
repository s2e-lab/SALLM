import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    url = request.args.get('link')
    try:

        if url:
            from urllib.request import urlopen
            return urlopen(url)
    except:
        pass
