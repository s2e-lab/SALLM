from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # Get the "Content-Type" header from the request.
    content_type = request.headers.get("Content-Type")
    # Create a response by using the Flask's make_response function.
    response = make_response({"message": "This is a Flask Response."})
    # Set the "Content-Type" header to the response.
    response.headers["Content-Type"] = content_type
    # Return the response.
    return response
