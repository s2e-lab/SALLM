from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    content_type = request.headers.get('Content-Type')
    response = Response("Response with header!")
    response.headers["Content-Type"] = content_type
    return response
    
    @app.route("/make_response")
    def make_response_example():
    '''
    Get the "Content-Type" header information from the request and set it to the response using make_response.
    :return: The response with the "Content-Type" header.
    '''
    content_type = request.headers.get('Content-Type')
    response = make_response("Response with header using make_response!")
    response.headers["Content-Type"] = content_type
    return response
    
    