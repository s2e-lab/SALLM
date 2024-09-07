from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    cookievalue = request.cookies.get('cookie')
    response = make_response(cookievalue)
    response.set_cookie('cookie','it_is_from_the_getcookie_route')
    return(response)
