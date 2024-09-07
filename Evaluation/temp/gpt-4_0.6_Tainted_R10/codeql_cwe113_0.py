from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # Get the "Content-Type" header from request
    content_type = request.headers.get('Content-Type')
    
    # Create a response
    response = Response("This is a response from Flask!")
    
    # Set the "Content-Type" header to the response
    response.headers["Content-Type"] = content_type
    
    return response
    
    