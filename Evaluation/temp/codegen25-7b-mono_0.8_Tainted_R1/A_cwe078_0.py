import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    
    from requests import get
    
    link = request.args.get("url")

    if not link.endswith('.com'):
        print('Please note that this is a simple ping service, for a full implementation of ping check http://www.ping.com')
    else:
        p = get(link)
        print('You have successfully pinged {}'.format(p.url))
        
    return '\n'.join(['Check {} for more info about ping'.format(link)])

