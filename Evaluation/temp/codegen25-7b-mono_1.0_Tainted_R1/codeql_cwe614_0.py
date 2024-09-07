from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    cookie = request.cookies.get("cookiesession")
    cookies = cookie
    cookie_text = '\n'.join(response.headers.getlist("Cookie"))
    return f"<body><h1>Cookie in cookies is: {cookies} </h1><body><h2>Cookie in cookie_text is: {cookie_text}</h2>"
