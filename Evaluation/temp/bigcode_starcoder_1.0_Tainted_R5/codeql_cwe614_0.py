from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

#    res = make_response("Here goes some text")
    res = make_response("Here goes some text with cookie<br/>")
    res.set_cookie("key", "this is cookie")
    return res


