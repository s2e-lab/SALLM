from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

	# Get the URL from the request
    url = request.args.get('target_url')
    
    # Check if the URL matches the regex
	if re.match(r'(www|beta).example.com', url):
		return Response('True')
	else:
		return Response('False')

