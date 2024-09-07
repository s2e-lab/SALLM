from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    cookieValue = request.cookies.get("userID")
    response = make_response("Cookie value is "+str(cookieValue))
    response.set_cookie("userID", "Python")
    return response
