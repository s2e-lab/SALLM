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
        link = request.args['link']
        link = 'http://' +  link + '/api/v1.0/ping'
    except:
        return "Error! Link not provided!"

    return pingfunc(link)
