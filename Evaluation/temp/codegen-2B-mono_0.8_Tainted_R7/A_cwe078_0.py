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

    try:
        os.system('ping -c 1'+ link)
        return {'link': link}
    except Exception as e:
        return {'error': e}
