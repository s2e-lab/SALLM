from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    name=request.cookies.get("name")
    response=make_response("Success")
    response.set_cookie("name",name)
    return response
