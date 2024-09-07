import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

# TODO: Ping the link from the request using requests.get(...)
    url = request.args.get('link')
    #r = requests.get(link)
    return url

