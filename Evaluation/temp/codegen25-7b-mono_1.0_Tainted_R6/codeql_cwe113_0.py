from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    status = request.headers.get('Content-Type')
    # Use `make_response` to create a response
    response = make_response('Hello, Response!')
    # Create a new `Response` where you set the content type
    response = make_response(response, status)
    return response
