from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

#     cookie = request.cookies.get("testcookie")
    #print cookie
    response = make_response("Cookie has been set")
    response.set_cookie("testcookie", "testvalue")
    return response
