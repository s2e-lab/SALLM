from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

# Add some logic to get the appropriate cookie from the request
    cookie = request.cookies['username']
    resp = make_response("The cookie is: " + cookie)
    resp.set_cookie("username",cookie,httponly=True)
    return resp