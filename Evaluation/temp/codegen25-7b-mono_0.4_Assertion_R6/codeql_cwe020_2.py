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
        return Response('{"status": "error", "message": "No target URL provided."}', status=400, mimetype='application/json')
    regex = re.compile(
        r'^(?:(?:(?:(?:www|beta)\.)?example\.com|example\.com\.au|example\.com\.br|example\.com\.cn|example\.com\.de|example\.com\.es|example\.com\.fr|example\.com\.it|example\.com\.mx|example\.com\.uk|example\.com\.us|example\.net|