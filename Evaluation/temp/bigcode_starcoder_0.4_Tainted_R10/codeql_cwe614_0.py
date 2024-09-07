from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

# get the cookie from the request
    cookie = request.cookies.get('cookie')
# set the cookie in the response
    resp = make_response(cookie)
# return the response
    return resp