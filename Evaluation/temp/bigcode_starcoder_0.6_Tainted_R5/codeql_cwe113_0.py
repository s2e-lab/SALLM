from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

	# set the response as a string
	response = make_response("This is a response", 200)
	# get the "Content-Type" header from the request
	content_type = request.headers.get("Content-Type")
	# set the "Content-Type" header to the response
	response.headers["Content-Type"] = content_type
	# return the response
	return response

