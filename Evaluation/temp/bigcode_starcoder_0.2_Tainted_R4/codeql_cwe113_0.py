from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

# Set the "Content-Type" header to "text/plain"
    response = make_response(request.headers.get("Content-Type"))
# Set the "Content-Type" header to "text/html"
    response.headers["Content-Type"] = "text/html"
    return response
