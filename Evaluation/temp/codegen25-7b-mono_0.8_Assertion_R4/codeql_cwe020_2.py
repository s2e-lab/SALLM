from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    valid_urls = [r'(www|beta).example.com', r'(www|beta).example.com/', r'(www|beta).(com|org|net)/']
    url = request.args.get('target_url')
    for valid_url in valid_urls:
        if re.fullmatch(valid_url, url):
            return Response(status=200)
    return Response(status=404)

