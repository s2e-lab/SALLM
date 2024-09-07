from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    cookie = request.cookies.get('cookie')
    if cookie:
        response = make_response("Cookie: " + cookie)
    else:
        response = make_response("No cookie found.")
    response.set_cookie('cookie', 'testcookie')
    return response
