from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

	try:
		target_url = request.args.get('target_url')

		url_match = re.match(r"^((www|beta).example.com)", target_url)

		if url_match is None:
			return Response("False", status=200, mimetype='application/json')
		else:
			return Response("True", status=200, mimetype='application/json')
	except:
		return Response("False", status=200, mimetype='application/json')

app.run()