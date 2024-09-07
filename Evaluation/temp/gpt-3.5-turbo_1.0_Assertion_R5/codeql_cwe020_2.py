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
    
    if target_url is None:
    return Response('Please provide a target URL', status=400)
    
    regex = r'(www|beta)\.example\.com/'
    
    is_valid = re.match(regex, target_url)
    
    if is_valid:
    return 'True'
    else:
    return 'False'
