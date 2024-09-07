from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    # Get the cookie data and set it as a cookie in the response.
    cookie = request.cookies.get("cookie")
    response = make_response("The cookie is {}".format(cookie))
    response.set_cookie("cookie", cookie)
    return response
