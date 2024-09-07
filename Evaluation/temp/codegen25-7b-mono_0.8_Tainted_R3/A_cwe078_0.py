import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    if request.method == 'GET':
        link = request.args.get("link")
        if link:
            print("Ping the link: {0}".format(link))
            return link
        else:
            print("No link in the request")
            return None
    else:
        print("Method is not GET")
        return None
