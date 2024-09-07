from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    target_url = request.args.get('url')
    url_regex = re.compile(r'^(www|beta)(\d*)?(?=.)(http[|s]*):\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$')
    
    if url_regex.match(target_url):
        return Response(True, status = 200, mimetype= 'application/json')
    else:
