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
    
    # check if target_url is not None
    if target_url:
        # regex pattern for valid URL
        pattern = r'^(www|beta)\.example\.com/$'
    
        # check if target_url matches the pattern
        if re.match(pattern, target_url):
            return 'True'
        else:
            return 'False'
    else:
        return 'False'
