from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    # Fetch target_url from request's query parameters
    target_url = request.args.get('target_url')
    
    # Define the URL pattern
    url_pattern = r"(www|beta)\.example\.com/"
    
    # Check if target_url matches with url_pattern
    if re.match(url_pattern, target_url):
        # If match is found, the URL is valid
        return Response('True', status=200)
    else:
        # If no match is found, the URL is invalid
        return Response('False', status=400)
    
    
    