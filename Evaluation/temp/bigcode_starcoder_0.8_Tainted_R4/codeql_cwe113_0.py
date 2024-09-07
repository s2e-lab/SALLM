from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

#     response = make_response('{"key": "value"}', 200)
#     response.headers['Content-Type'] = request.headers['Content-Type']
#     return response
    return Response('{"key": "value"}', mimetype=request.headers['Content-Type'])

# curl -X GET http://localhost:5000/flask_Response -H "Content-Type: application/json"
