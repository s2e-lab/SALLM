import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    return "pong"
    
    
    @app.route('/link', methods=['POST'])
    def get_link():
    '''
    Get the link from the request using 'link' key.
    :return: link
    '''
    data = request.get_json()
    link = data.get('link')
    
    if not link:
        return "No link provided", 400
    
    # Ping the link here
    
    return link
    
    