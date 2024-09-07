from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

#    resp = Response(response='Hello World', status=200)
#    resp.headers['Content-Type'] = request.headers['Content-Type']
#    return resp
    resp = make_response('Hello World', 200)
    resp.headers['Content-Type'] = request.headers['Content-Type']
    return resp
