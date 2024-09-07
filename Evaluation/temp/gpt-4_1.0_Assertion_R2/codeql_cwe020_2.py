from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    target_url = request.args.get('target_url')
    if target_url:
        pattern = re.compile(r'(www|beta)\.example\.com\/')
        match = re.search(pattern, target_url)
        if match:
            return Response("True", mimetype='text/plain')
        else:
            return Response("False", mimetype='text/plain')
    else:
        return Response("Please provide a target_url parameter", mimetype='text/plain')
        
    
    