import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    link = request.args.get('link', None)
    if link is None:
        return "No link in the request"
    else:
        if os.system('ping {}'.format(link)) == 0:
            return "OK, the link is reachable"
        else:
            return "Link is unreachable"
