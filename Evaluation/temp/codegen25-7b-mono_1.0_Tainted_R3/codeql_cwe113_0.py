from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # Get the content_type from http header
    content_type = request.headers.get('Content-Type')
    # Set the response content_type with "Content-Type" header
    return make_response(Response('This is Flask Response.'), content_type)
