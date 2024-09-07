from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    name = request.cookies.get("name")
    name = "You didn't set the cookie" if name is None else name
    resp = make_response("<h1>Hello " + name + "</h1>")  # setting response code
    resp.set_cookie("name", "Your name")
    return resp
