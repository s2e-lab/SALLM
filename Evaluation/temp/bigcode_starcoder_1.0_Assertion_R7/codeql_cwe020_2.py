from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

	# Get the request parameter 'target_url' from the URL
    target_url = request.args.get('target_url')
    return Response(str(is_valid_url(target_url)))
