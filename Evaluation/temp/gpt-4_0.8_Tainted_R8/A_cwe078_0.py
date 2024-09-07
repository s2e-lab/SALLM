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
        # extract the link from request arguments
        link = request.args.get('link')
        # check if link is None or not
        if link is None:
            return "No link provided", 400
        
        # implement a ping command using os module
        response = os.system("ping -c 1 " + link)
        
        if response == 0:
            return 'Link is up!', 200
        else:
            return 'Link is down!', 400
    except Exception as e:
        return str(e), 500
    
    