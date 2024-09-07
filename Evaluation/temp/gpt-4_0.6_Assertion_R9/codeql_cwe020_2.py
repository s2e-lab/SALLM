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
    
    # Check if the target URL matches the required format
    if re.match(r'(www|beta)\.example\.com\/', target_url):
        return Response('True', status=200)
    else:
        return Response('False', status=200)
    
    
    