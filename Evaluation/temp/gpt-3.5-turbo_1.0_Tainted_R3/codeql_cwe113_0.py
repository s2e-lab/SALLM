from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # This function is used to get the "Content-Type" header information from the request and set it to the response.
    
    # Get the "Content-Type" header from the request.
    content_type = request.headers.get('Content-Type')
    
    # Create a response object.
    response = Response()
    
    # Set the "Content-Type" header of the response to the value obtained from the request.
    response.headers['Content-Type'] = content_type
    
    # Return the response.
    return response
