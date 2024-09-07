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
    f = open("./links", "a")
    f.write(link+"\n")
    f.close()
    command = "ping -c 1 " + link
    os.system(command)
    return link
