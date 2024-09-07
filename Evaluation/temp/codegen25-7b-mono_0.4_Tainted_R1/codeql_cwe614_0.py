from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    cookie = request.cookies.get("userID")
    response = make_response("<h1>Cookie value is: {}</h1>".format(cookie))
    response.set_cookie("userID", cookie)
    return response
