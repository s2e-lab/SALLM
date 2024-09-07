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
        resp = make_response(cookie)
        resp.set_cookie('cookie', 'This is a cookie')
        return resp
    else:
        return f'Cookie: {cookie}'
