from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # Get the headers from the request
    response_header = request.headers.get("Content-Type")
    
    # Create an HTTP Response and set the Content-Type header (note that we also need to convert the variable from text to bytes)
    response = Response("This example is not for web servers", mimetype=response_header)
    response.headers["Content-Type"] = response_header
    
    return response
