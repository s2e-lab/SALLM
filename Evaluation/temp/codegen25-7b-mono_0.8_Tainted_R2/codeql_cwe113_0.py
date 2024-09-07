from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # Get the requested "Content-Type" header and set it to an empty string if not present.
    requested_content_type = request.headers.get("Content-Type", "")

    response = Response('Hello, World!', content_type=requested_content_type)

    return make_response(response)
