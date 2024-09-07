from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    target_url = request.args.get('target_url', '')
    url_pattern = r'^(http(s?)://)?(www|beta)\.example\.com(/.*)?$'
    if re.fullmatch(url_pattern, target_url):
        return Response('True', mimetype='application/text')
    else:
        return Response('False', mimetype='application/text')
    
    
    