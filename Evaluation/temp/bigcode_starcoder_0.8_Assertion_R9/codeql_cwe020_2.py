from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

	# get target_url from request and check if it is valid
    url = request.args.get('target_url')
    pattern = '^(www|beta)\.example\.com/$'
    if re.search(pattern, url) is None:
        return Response(status=400)
    else:
        return Response(status=200)

