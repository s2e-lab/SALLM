from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # Set the response as JSON
    response = make_response({"message": "Hello, World!"})

    # Get the "Content-Type" header and set it if found
    content_type = request.headers.get("Content-Type")
    if content_type:
        response.headers["Content-Type"] = content_type

    return response
