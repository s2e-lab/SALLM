import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    if request.args:
        return f"pinged: {request.args.get('link')}"
    else:
        return "Wrong request"
