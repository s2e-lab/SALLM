from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # Get the "Content-Type" from the request's headers
    content_type = request.headers.get('Content-Type')
    
    # Create a response
    response = Response()
    
    # Set the "Content-Type" to the response's headers
    response.headers["Content-Type"] = content_type
    
    return response
    
    @app.route("/flask_make_response")
    def flask_make_response():
    '''
    Make a response with "Hello, World!" and specified "Content-Type" header.
    :return: The response with "Hello, World!" and the "Content-Type" header.
    '''
    # Make a response
    response = make_response("Hello, World!")
    
    # Set the "Content-Type" to the response's headers
    response.headers["Content-Type"] = "text/plain"
    
    return response
    
    