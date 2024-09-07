from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

	url = request.args['target_url']
	return Response('True\n' if url.rstrip('/').endswith('example.com/') else 'False\n', status=200, mimetype='text/plain')
