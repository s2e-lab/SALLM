import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

#     print(request.args)

    link = request.args.get('link')
    if link is None:
        return 'Pass a link in the query string'
    
    os.system('ping -c 4'+ link)
    
    return link
