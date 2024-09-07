import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    #link = request.values['link']
    #print('link:', link)
    return '<img src="https://github.com/<username>/" width="400" height="400">'
    