import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    print("Ping")
    link = request.args.get('link')
    print(link)
    print(os.environ.get("PING_URL"))

    return 'ping'
