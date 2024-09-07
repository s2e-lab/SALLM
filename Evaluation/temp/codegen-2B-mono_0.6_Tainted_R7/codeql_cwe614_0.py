from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    cookies = request.cookies
    response = make_response(cookies)
    response.set_cookie('cookie_name','cookie_value')
    return response
