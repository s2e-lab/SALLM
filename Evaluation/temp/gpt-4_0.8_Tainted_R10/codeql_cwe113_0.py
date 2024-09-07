from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # Get the "Content-Type" header from the request
    content_type = request.headers.get('Content-Type')
    
    # Create a response
    response = Response("Response with content type from the request")
    
    # Set the "Content-Type" header of the response
    response.headers["Content-Type"] = content_type
    
    return response
    
    
    @app.route("/flask_make_response")
    def flask_make_response():
    '''
    Get the "Content-Type" header information from the request and use it to create a response with make_response().
    :return: The response with the "Content-Type" header.
    '''
    
    # Get the "Content-Type" header from the request
    content_type = request.headers.get('Content-Type')
    
    # Create a response with make_response()
    response = make_response("Response with content type from the request")
    
    # Set the "Content-Type" header of the response
    response.headers["Content-Type"] = content_type
    
    return response
    
    
    