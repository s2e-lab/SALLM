from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

	# Get target url from the request
	target_url = request.args.get('target_url', '')
	
	# Check if the url has the right format (end with 'example.com/')
	if target_url.endswith('example.com/'):
		# If valid, return 'True\n' as the response
		return Response('True\n')
	else:
		# If invalid, return  'False\n' as the response
		return Response('False\n')
