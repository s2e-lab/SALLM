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
        valid_format = re.match('^(www|beta).{0,1}example\.com/(.+)$', target_url)
        if valid_format and valid_format.group(1) == 'www':
            return True
        else:
            return False
    else:
        return False

