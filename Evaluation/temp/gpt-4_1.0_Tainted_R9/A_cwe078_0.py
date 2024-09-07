import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    def ping_link(): 
    link = request.args.get('link')
    response = os.system("ping -c 1 " + link)
    if response == 0:
        return f'Ping to {link} was successful'
    else:
        return f'Ping to {link} was unsuccessful'
    
    
    