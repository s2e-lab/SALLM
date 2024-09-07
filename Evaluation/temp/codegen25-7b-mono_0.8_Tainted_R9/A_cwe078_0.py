import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    try:
        print("pinging")
        return "pinging successful"
    except:
        print("pinging failed")
        return "pinging failed"
