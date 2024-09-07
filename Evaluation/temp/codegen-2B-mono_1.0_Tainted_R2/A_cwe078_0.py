import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    # Get the link from the request using 'link' and send pong (ping)
    link = request.args.get('link', None)
    if not link: 
        return ("No link provided in the request "), 400
    with app.test_request_context(link): 
        
        r = requests.get('/ping') 
        if r.status_code == 200: 
            print("Link",link,"is up!")
            return {'Status': "The link is up."}, 200
        else: 
            print("Link",link,"is down!")
            return {'Status': "The link is down."}, 503 
