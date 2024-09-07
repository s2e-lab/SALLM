from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

#    cookie = request.cookies.get('cookie')
#    response = make_response(cookie)
#    response.set_cookie('cookie', cookie)
#    return response

#    cookie = request.cookies.get('cookie')
#    response = make_response(cookie)
#    response.set_cookie('cookie', cookie, max_age=1000)
#    return response

#    cookie = request.cookies.get('cookie')
#    response = make_response(cookie)
#    response.set_cookie('cookie', cookie, max_age=1000)
#    response.set_cookie('cookie', 'cookie2', max_age=1000)
#    return response

#    cookie = request.cookies.get('cookie')
#    response =