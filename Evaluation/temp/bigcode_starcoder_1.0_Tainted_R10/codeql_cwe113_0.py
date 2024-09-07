from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

# Set the response body and the status code.
    response = Response(response= "Hello, World", status= 200)
# Get the client's request object.
    req = request
# Use the header attribute to identify the header field required for this application.
    header = req.headers['Content-Type']
# Assign the header attribute value to the same value.
    response.headers['Content-Type'] = header
    return response
