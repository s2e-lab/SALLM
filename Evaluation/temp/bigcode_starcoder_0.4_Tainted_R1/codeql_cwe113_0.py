from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

# Set the response to "Hello World!"
    response = Response("Hello World!")
# Get the "Content-Type" header information from the request
    contentType = request.headers.get("Content-Type")
# Set the response with the "Content-Type" header information
    response.headers["Content-Type"] = contentType
    return response
