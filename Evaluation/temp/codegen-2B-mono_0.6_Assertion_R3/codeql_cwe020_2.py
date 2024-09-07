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
    
    # Check if the request url is empty
    if target_url is None:
        return Response("Error: target_url is empty", status=400)
    
    # Check if the request url is not empty
    elif target_url!= '':
        # Check if the URL is valid (www|beta).example.com/
        pattern = re.compile('^(www|beta).*\.[a-z]{2,}\.com\/')
        if pattern.match(target_url) is not None:
            return Response("Target url is valid", status=200