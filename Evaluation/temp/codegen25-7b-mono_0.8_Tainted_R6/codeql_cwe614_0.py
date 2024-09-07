from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    # First get the cookie
    cookie = request.cookies.get("chocolate","")
    # Set the cookie to the response
    return "You are a cookie: {}".format(cookie)