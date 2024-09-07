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
    
    response = os.system("ping -c 1 " + link)
    
    if response == 0:
        return f'Ping to {link} is successful!', 200
    else:
        return f'Ping to {link} has failed!', 400
    
    