from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    response_object = Response()
    response_object.headers["Access-Control-Allow-Origin"] = "*"
    response_object.headers["Access-Control-Allow-Credentials"] = True
    response_object.headers["Access-Control-Allow-Headers"] = "x-requested-with, content-type"
    response_object.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response_object.headers['Access-Control-Expose-Headers'] = 'Authorization'
    response_object.data = 'This is plain text but it is in bytes'
    response_object.set_cookie("auth", "0")
    return response_object
