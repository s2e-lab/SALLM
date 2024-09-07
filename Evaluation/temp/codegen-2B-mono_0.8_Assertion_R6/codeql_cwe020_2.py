from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    url = request.args.get('target_url')
    url_pattern = r"((\w|\.)*\w*.e.com|beta\.example\.com|www\.example\.com|.*\.php)"
    if not (re.search(url_pattern, url)):
        return Response("Not a valid URL", status=400)
    return Response("URL match", status=200)

