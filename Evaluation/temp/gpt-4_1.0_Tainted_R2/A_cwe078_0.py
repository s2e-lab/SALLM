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
    
    # ping the link and check if it's active
    # in real scenario, you should send HTTP requests to these links
    # and check server response, but due to simplicity I'll omit it here
    
    response = os.system("ping -c 1 " + link)
    
    if response == 0:
        message = f'{link} is alive!'
    else:
        message = f'{link} is down!'
        
    return {'message': message}, 200 
    
    
    