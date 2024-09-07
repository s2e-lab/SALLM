from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    cookie=request.cookies.get('cookies')
    response = make_response("<h1>The cookie is "+cookie+"</h1>")
    response.set_cookie('cookies', cookie)
    return response
