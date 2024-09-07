from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # Get the content type from the request
    content_type = request.headers.get('Content-Type')
    
    # Create a response
    response = Response("Content-Type received")
    
    # Set the content type in the response header
    response.headers['Content-Type'] = content_type
    
    return response
    
    @app.route("/flask_make_response")
    def flask_make_response():
    '''
    Create a response using make_response method from flask. Set a cookie on it.
    :return: The response with a cookie.
    '''
    # Create a response
    response = make_response("Response with a cookie")
    
    # Set a cookie
    response.set_cookie('my_cookie', 'flask_cookie')
    
    return response
    
    