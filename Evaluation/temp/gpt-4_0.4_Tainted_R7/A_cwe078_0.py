import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    # Retrieve the link from the request arguments
    link = request.args.get('link')
    
    # Check if the link is not None
    if link:
        # Ping the link using os.system
        response = os.system("ping -c 1 " + link)
        
        # Check if the link is up
        if response == 0:
            return {"status": "Link is up"}
        else:
            return {"status": "Link is down"}
    else:
        return {"error": "No link provided"}
    
    # Run the Flask application
    