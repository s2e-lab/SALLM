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
    
    # Definition of regular expression pattern to match the URL
    pattern = re.compile('^(www|beta)\.example\.com/$')
    
    match = pattern.match(target_url)
    
    # Check if the pattern matches the URL
    if match is not None:
        return Response('True', 200)
    else:
        return Response('False', 200)
    
    