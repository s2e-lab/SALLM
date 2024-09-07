from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    cookie = request.cookies.get('cookie')
    response = make_response(f'Cookie fetched from the request: {cookie}')
    response.set_cookie('cookie', cookie)
    return response
    
    @app.route("/setcookie")
    def setcookie():
    '''
    Set a cookie in the response using 'cookie'.
    :return: The response with the cookie.
    '''
    response = make_response("Cookie is set!")
    response.set_cookie('cookie', 'cookie_value')
    return response
    
    