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
        return Response(str(False), status=400)
    else:
        target_url_regex = re.compile(r"(www|beta)\.[a-zA-Z]+\.com(/[a-zA-Z0-9-_./]*)?")
        if target_url_regex.match(target_url):
            return Response(str(True), status=200)
        return Response(str(False), status=400)

