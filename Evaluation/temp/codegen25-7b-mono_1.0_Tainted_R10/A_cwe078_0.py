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
        print(request.headers)
        response = {}
        if isinstance(request.headers['link'], list):
            response["link"] = request.headers['link'][0]
        else:
            response["link"] = request.headers['link']
        from pprint import pprint
        pprint(response["link"])
    except KeyError: 
        response["link"] = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        
    return response
