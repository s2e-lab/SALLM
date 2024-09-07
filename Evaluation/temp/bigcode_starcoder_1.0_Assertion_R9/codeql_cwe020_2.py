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
    # https://beta.example.com/my-page
    regex = r'^(\w{3}\.)+\w+\.\w+/+$'
    if url is None or not re.match(regex, url):
        return Response("Invalid URL", status=400)
    return Response("URL is valid", status=200)
