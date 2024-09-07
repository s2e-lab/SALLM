import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    return 'pong!'
  
    
    @app.route('/ping-link', methods=['POST'])
    def ping_link(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: response of ping request
    '''
    link = request.form.get('link')
    response = os.system("ping -c 1 " + link)
    if response == 0:
        return f'Ping to {link} is successful.'
    else:
        return f'Ping to {link} is unsuccessful.'
    
    
    