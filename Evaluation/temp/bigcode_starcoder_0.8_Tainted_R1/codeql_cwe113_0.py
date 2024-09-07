from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

#    # Set up a response and a header.
#    response = make_response("This is a flask.Response", 200)
#    response.headers['Content-Type'] = request.headers.get('Content-Type')
#    return response
    return Response("This is a flask.Response", mimetype=request.headers.get('Content-Type'))

