from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    cookie = request.cookies.get('cookie')
    if cookie is None:
        cookie = 'No cookie found'
    else:
        cookie = 'Cookie found: ' + cookie
    
    response = make_response(cookie)
    response.set_cookie('cookie', 'test_cookie')
    
    return response
