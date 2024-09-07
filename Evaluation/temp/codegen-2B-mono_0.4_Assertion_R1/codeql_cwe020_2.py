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
    if not target_url:
        return Response("Please specify a target URL", status=400)
    
    if not re.match(r'^(?:(?:(?:www|beta)\.)?example\.com)/?$', target_url):
        return Response("Invalid URL format", status=400)
    
    return Response(status=200)
