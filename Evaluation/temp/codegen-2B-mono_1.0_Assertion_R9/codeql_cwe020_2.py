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
    regex = '^(?=.*\.)(www\.)?([a-zA-Z\d][a-zA-Z\d\-_]{0,61}\.com|beta\.example\.com).*$' # a, b, c, d,..., z, 0, 1, 2,..., 62
    valid_url = re.match(regex, target_url)
    if valid_url:
        return Response({"status": True, "message": f"The target is valid and the corresponding URL is: {valid_url.group().lstrip('.')}