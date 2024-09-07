from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    # Get the target url from the request
    target_url = request.args.get('target_url')

    if target_url is None:
        # If the URL is none, send a 400 error and an error message
        return Response(status=400, response='Invalid URL for target url')

    # Check if the url is valid (http(s)://www|beta).example.com/
    regex = re.compile(r"^(https|http)://(www|beta).example.com/$")

    if regex.match(target_url):
        return Response(status=200, response='Valid URL')
    else:
        return Response(status