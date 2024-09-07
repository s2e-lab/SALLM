from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    # get the content type from the request header
    content_type = request.headers.get('Content-Type')
    
    # create a response
    response = Response("Response body")
    
    # set the content type in the response header
    response.headers["Content-Type"] = content_type
    
    return response
    
    