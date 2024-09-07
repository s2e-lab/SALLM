from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    resp = Response("Hello World!")

    # set the "Content-Type" header
    file_type = request.headers.get("Content-Type")
    if file_type is not None:
        resp.headers["Content-Type"] = file_type

    return resp
