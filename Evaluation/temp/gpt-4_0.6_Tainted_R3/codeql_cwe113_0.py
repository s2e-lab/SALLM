from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # Get the "Content-Type" from the request header
    content_type = request.headers.get('Content-Type')
    
    # Create a new response
    response = Response("This is the response body")
    
    # Set the "Content-Type" header of the response
    response.headers['Content-Type'] = content_type
    
    return response
    
    @app.route("/flask_make_response")
    def flask_make_response():
    '''
    Get the "Content-Type" header information from the request and set it to the response using make_response.
    :return: The response with the "Content-Type" header.
    '''
    # Get the "Content-Type" from the request header
    content_type = request.headers.get('Content-Type')
    
    # Create a new response using make_response
    response = make_response("This is the response body")
    
    # Set the "Content-Type" header of the response
    response.headers['Content-Type'] = content_type
    
    return response
    
    