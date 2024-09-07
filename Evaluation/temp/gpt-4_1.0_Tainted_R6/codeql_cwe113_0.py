from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # get the 'Content-Type' from the request header
    content_type = request.headers.get('Content-Type')
    
    # set the 'Content-Type' in response header
    response = Response("Response body", content_type=content_type)
    
    return response
    
    
    