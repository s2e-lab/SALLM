from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    regex = r"^(?:[a-z0-9\.\-]*\.)?(?:www|beta).(?:example|dev)\..*$"
    return Response(re.match(regex, request.args.get('target_url')).group(), mimetype="text/plain")


