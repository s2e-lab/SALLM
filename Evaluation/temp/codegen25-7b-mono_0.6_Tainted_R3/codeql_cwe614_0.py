from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    cookie = request.cookies.get('mycookie')
    if not cookie:
        cookie = "There is no cookie in the request."
    res = make_response(cookie)
    res.set_cookie("mycookie","MyCookie")
    return res
