import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

#    return "The ping got a ping and a ping went to " + request.args.get('link')
    return request.args.get('link')
