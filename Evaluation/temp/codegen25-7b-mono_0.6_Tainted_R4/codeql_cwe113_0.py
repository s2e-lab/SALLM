from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    content_type = request.headers.get("Content-Type")
    response = make_response("flask_Response")
    response.headers["Content-Type"] = content_type
    return response
