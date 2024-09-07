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
    if link is None:
        link = "http://www.google.com"
    else:
        link = link
    cmd = 'ping -c1 ' + link
    response = os.popen(cmd).read()
    return response
