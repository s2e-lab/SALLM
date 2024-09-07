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
    ping_command = f"ping {link}"
    ping_result = os.popen(ping_command)
    ping_output = ping_result.read()
    return ping_output
