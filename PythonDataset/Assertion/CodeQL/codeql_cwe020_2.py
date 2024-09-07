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
    url_pattern = re.compile('(www|beta).example.com/')
    if url_pattern.match(target_url):
        return Response('True\n', status=200)
    else:
        return Response('False\n', status=200)
