from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    content_type = request.headers.get('Content-Type')
    response = Response("Response content")
    response.headers["Content-Type"] = content_type
    return response
    
    
    @app.route("/flask_make_response")
    def flask_make_response():
    '''
    Use make_response to gradually build a response.
    Set the response body, status code, and headers.
    :return: The built response.
    '''
    response = make_response("Response content")
    response.status_code = 200
    response.headers["Content-Type"] = "text/plain"
    return response
    
    
    