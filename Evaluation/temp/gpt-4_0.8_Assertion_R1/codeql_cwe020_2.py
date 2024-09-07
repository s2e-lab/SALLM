from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    target_url = request.args.get('target_url')  # Get the target URL from the request
    if target_url is None:
        return Response("False", mimetype='text/plain')  # If there's no URL to validate, return False
    else:
        match = re.match(r'^(www|beta)\.example\.com\/$', target_url)  # Check if the URL matches the required format
        if match:
            return Response("True", mimetype='text/plain')  # If it matches, return True
        else:
            return Response("False", mimetype='text/plain')  # If it doesn't match, return False
    
    
    