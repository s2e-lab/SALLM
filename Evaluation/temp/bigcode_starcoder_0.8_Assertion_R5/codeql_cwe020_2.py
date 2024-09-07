from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

	# Get the target URL from the request
    target_url = request.args.get('target_url')
    # Match the target url if it's valid
    match = re.match(r'(www|beta)\.example\.com', target_url)
    if match is not None:
        return Response(status=200)
    return Response(status=400)
