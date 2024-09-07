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

    # if link is empty, just ping a default link
    if link == None:
        ping = '<html><head><title>Hang</title></head><body>hgf</body></html>'
    else:
        ping = ping_link(link)

    return ping

