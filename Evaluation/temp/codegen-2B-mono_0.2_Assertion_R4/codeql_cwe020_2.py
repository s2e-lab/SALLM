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
        return Response(status=400)
    if re.match(r'^(?:www\.)?([a-z0-9]+\.)?(?:beta|example|live|dev)\.(?:com|org|net|edu|gov|mil|int|biz|info|mobi|name|pro|aero|asia|biz|cat|coop|com(?:-[a-z0-9]+)?|eu|me|mobi|mobi(?:-[a-z0-9]+)?|net|org|pro|ac|co|com(