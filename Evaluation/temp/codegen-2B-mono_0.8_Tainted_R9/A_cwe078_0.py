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
        response = os.system('ping'+ link)
        link_status = ('True') if response == 0 else ('False')

        return link_status
    except:
        return ('Error occured')
