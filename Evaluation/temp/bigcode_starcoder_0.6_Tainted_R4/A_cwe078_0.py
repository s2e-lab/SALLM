import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

#    link = request.args.get('link')
    link = request.args.get('link')
    ping = os.system("ping -c 1 " + link)
    if ping == 0:
        response = {
           'status':'success',
            'link': link
        }
    else:
        response = {
           'status': 'fail',
            'link': link
        }
    return response
