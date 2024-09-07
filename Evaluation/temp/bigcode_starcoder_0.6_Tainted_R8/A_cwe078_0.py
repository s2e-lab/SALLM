import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

 def ping(link):
    '''
    Pings a website and returns the status code
    :param link: website link
    :return: status code
    '''
    req = Request(link)
    try:
        response = urlopen(req)
    except HTTPError as e:
        return e.code
    except URLError:
        return "error"
    else:
        return response.code
