from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

	response = Response("Hello World")
	# Get the "Content-Type" header information from the request and set it to the response.
	content_type = request.headers.get('content-type')
	if content_type:
		response.headers['content-type'] = content_type
	else:
		response.headers['content-type'] = 'application/octet-stream'
	return response

