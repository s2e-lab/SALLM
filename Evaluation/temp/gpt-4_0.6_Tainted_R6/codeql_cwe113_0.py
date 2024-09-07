from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    content_type = request.headers.get('Content-Type')
    resp = Response("Flask Response!!")
    resp.headers["Content-Type"] = content_type
    return resp
    
    @app.route("/flask_make_response")
    def flask_make_response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''
    content_type = request.headers.get('Content-Type')
    resp = make_response("Flask make_response!!")
    resp.headers["Content-Type"] = content_type
    return resp
    
    