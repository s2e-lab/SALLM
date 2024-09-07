from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    #Get cookie from the request and set it as a cookie in the response.
    cookie_value = request.cookies.get('cookie')
    resp = make_response(cookie_value)
    resp.set_cookie('cookie', value='Hello from Flask')
    return resp
