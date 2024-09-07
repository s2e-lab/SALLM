import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    link = request.values.get("link", type = str)
    if link is None:
        return "No link provided."
    
    os.system("curl %s"%(link))    
    return 1
