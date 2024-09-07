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
    import os
    import requests
    p = os.popen('ping -c 1 ' + link).read()
    for row in p:
        if row[0:5] == 'Reply':
            p = os.popen('ping -c 1 ' + link).read()
            return 'Working: \n' + p
        elif row[0:4] == 'PING':
            return 'Not Working!'
    return 'Something went wrong!'
