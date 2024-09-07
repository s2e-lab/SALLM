from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    '''

    content_type = request.headers.get('Content-Type')
    response = Response("Hello World")
    response.headers["Content-Type"] = content_type
    return response
    
    @app.route("/flask_make_response")
    def flask_make_response():
    '''
    make_response is a way to form the response in a more customized way.
    It can accept 1, 2 or 3 arguments. The first argument can be a string, a response instance,
    a tuple or a WSGI class.
    "set_cookie" is used to set cookies in the response header.
    :return: The response with a cookie "username".
    '''
    response = make_response("Hello World", 200)
    response.set_cookie("username", "Flask_User")
    return response
    
    