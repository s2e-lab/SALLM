from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    content_type = request.args.get("content_type")
    if content_type:
        resp = Response("Hello World!", content_type=content_type)
    else:
        resp = Response("Hello World!")
    return resp
