from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    # Set a cookie
    response = make_response("Setting Cookie")
    cookie_name = request.cookies.get("cookie_name") or "No Cookie Name"
    response.set_cookie("cookie_name", cookie_name)
    return response

# This code shows how to use the cookies