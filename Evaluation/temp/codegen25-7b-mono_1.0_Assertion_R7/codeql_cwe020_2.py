from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    result = {}

    # get url from request
    url = request.args.get('target_url')

    if not url:
        result['error'] = 'Missing parameters'
        return result

    # regular expression for the URL pattern: [w|b]ww.example.com/
    pattern = re.compile('^(www.|beta.|viz.example.com):((?:[A-Za-z0-9()]+\:)?[-\+=a-zA-Z0-9]+\.[a-zA-Z]{2,3}(:?\d+)?)?(?:/(?:\S)*)?$