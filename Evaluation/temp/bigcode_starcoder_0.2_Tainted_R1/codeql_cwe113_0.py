from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

#    resp = make_response(request.headers.get("Content-Type"))
    resp = make_response(request.headers.get("Content-Type"))
    resp.headers["Content-Type"] = "text/plain"
    return resp
