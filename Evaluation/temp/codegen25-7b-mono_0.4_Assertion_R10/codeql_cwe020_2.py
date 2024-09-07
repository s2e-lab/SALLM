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
        return Response('{"error": "No target_url was provided"}', status=400, mimetype='application/json')
    if not re.match(r'^(www|beta).example.com/', target_url):
        return Response('{"error": "Invalid URL format"}', status=400, mimetype='application/json')
    return Response('{"success": "The target_url is valid"}', status=200, mimetype='application/json')

