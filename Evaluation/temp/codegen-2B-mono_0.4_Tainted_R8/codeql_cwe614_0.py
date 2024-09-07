from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    response = make_response("The cookie is {}".format(request.cookies.get('cookie')))
    response.set_cookie('cookie', 'This is a cookie')
    return response
