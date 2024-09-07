from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

	# get the request header
    request_header = request.headers

    # set the response header
    response_header = {
        "Content-Type": request_header["Content-Type"]
    }

    # set the response body
    response_body = "flask_Response"

    # return the response
    return Response(response=response_body, status=200, headers=response_header)
