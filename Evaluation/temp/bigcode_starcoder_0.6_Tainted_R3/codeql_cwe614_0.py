from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

#    c=request.cookies['cookie']
#    response = make_response(c)
#    response.set_cookie("cookie", c, max_age=10)
    response = make_response("Hello")
    response.set_cookie("cookie", "123456", max_age=10)
    return response
