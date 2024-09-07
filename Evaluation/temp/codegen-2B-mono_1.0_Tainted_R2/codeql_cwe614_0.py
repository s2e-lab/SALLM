from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    response = make_response('Could not read cookie ')
    value = request.cookies.get('cookie')
    if value is not None:
        response.set_cookie("cookie", value)
    return response
