import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

<<<<<<< HEAD
    return "pong"
=======
    link = request.args.get('link')
    link = 'http://www.google.com'
    os.system('ping -c 1'+ link)
    return link
>>>>>>> 705d1c79846a913157f93718743164c0e6251a84
