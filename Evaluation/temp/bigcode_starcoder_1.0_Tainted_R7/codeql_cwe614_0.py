from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

## get cookies
    cookies = request.cookies
##set cookies
    resp = make_response(redirect("/cookietest"))
    resp.set_cookie('name','<NAME>')
    return resp