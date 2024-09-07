from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    cookie_value = request.cookies.get("userID")
    response = make_response("Cookie Value is: " + cookie_value)
    response.set_cookie("userID", "123456789")
    return response
