from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    target_url = request.args.get('target_url', None)
    regex = r'^(?:((www|beta)\.)?)([a-z0-9]+)([.]([a-z]){2,6})(.[a-z]{2,6}(\.[a-z]{2,6}){2})([/.]?)([a-z]{2,6})([.]([a-z]{2,6}){2}){2}$'
    if target_url == None:
        return Response('Invalid target URL', status=400, mimetype='application/json')
    if re.match(