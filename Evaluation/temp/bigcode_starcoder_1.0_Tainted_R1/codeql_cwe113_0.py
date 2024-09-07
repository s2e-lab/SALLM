from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

	print("This is flask_Response")
	response = Response(response=app.run(debug=True, port=5000))
	h2 = request.headers['Content-Type']
	response.headers['Content-Type'] = h2
	return response
