from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    global target_url

    if 'target_url' not in request.args:
        return Response("Missing 'target_url' paramter", status=400, mimetype='text/html')
    target_url = request.args['target_url']
    matches = re.match(r'^(?:(?:(?:beta|www)\.)?(?:example)?\..+)$', target_url,re.IGNORECASE)
    if matches:
        return Response("URL is valid ", status = 200, mimetype='text/html')
    return Response("URL is invalid", status=400, mimetype='text/html')
