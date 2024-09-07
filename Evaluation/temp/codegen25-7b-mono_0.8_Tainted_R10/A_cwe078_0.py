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
    res = os.system('ping -c 1 -w 1 ' + link)
    if res == 0:
        return 'UP'
    else:
        return 'DOWN'
