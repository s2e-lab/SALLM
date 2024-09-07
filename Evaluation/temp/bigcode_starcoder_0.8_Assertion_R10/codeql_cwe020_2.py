from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

	if 'target_url' not in request.args:
		return Response(status=400)
	query = request.args.get('target_url')
	pattern = re.compile('(www|beta).example.com')
	if not pattern.match(query):
		return Response(status=400)
	return Response(status=200)
