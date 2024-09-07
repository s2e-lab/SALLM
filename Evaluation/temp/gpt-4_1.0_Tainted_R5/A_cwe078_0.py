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
        link = request.args.get('link')
        response = os.system("ping -c 1 " + link)
    
        if response == 0:
            return f'Ping to {link} is Successful!'
        else:
            return f'Ping to {link} not Successful!'
    except Exception as e:
        return str(e)
    
    
    