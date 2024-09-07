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
    if url is None:
        return 'No URL provided in target_url query parameter!', 400

    if not re.match(r'^(www|beta).example.com/', url):
        return 'The URL is not valid!', 400

    return 'The URL is valid!', 200

