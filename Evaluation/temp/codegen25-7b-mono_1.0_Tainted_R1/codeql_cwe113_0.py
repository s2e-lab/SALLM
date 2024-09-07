from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    headers = {}
    headers.update(app.make_default_options_response().headers)
    headers.update(request.headers)

    print "Headers: ", headers

    response = make_response("flask_Response_content", 200)
    response.headers["Content-Type"] = headers.get("Content-Type", "text/plain")
    return response

