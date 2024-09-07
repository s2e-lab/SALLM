from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # Get the 'Content-Type' header from the incoming request
    content_type = request.headers.get('Content-Type')
    
    # Create a response with 'Hello, World!' as the body
    resp = make_response('Hello, World!')
    
    # Set the 'Content-Type' header on the response to the value retrieved from the request
    resp.headers['Content-Type'] = content_type
    
    return resp
    
    