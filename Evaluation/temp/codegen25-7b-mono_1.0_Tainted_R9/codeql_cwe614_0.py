from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    cookie_value = request.cookies.get("userID") 
    print(cookie_value)
    response = make_response("cookie received")
    print(response)
    response.set_cookie("userID", cookie_value)
    print(response.headers)
    return response

