from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # get the "Content-Type" header information from the request
    content_type = request.headers.get("Content-Type")
    # set the "Content-Type" header information to the response
    response = make_response(content_type)
    return response
