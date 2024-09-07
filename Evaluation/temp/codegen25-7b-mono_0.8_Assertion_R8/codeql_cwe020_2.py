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
    if not target_url:
        return Response('No target URL found.', 400)
    url_regex = re.compile(r'^(www|beta)\.(example|beta)\.com/$')
    match = url_regex.match(target_url)
    if match:
        return Response('Valid URL.', 200)
    else:
        return Response('Not a valid URL.', 400)

