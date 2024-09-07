import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

#    link = request.args.get('link')
    link = 'https://www.linkedin.com/in/shubham-das-1212312/'
    import requests
    # Sending a GET request to the given URL
    r = requests.get(link)
    print(r.status_code)
    if r.status_code == 200:
        return link
    else:
        return 'Link not found'
