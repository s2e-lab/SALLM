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
      return f"Link {link} is up!"
    else:
      return f"Link {link} is down!', 404"
    
    