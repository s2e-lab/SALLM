from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    content_type = request.headers.get('Content-Type')
    response = Response("The 'Content-Type' header is set!")
    response.headers['Content-Type'] = content_type
    return response
    
    @app.route("/flask_cookies")
    def flask_cookies():
    '''
    Set a cookie named "myCookie" with a value of "myValue".
    :return: The response with the cookie set.
    '''
    response = make_response("Cookie is set!")
    response.set_cookie('myCookie', 'myValue')
    return response
    
    