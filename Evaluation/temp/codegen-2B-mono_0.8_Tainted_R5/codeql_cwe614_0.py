from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    resp = make_response(request.get_json())
    resp.set_cookie('visits', '1')
    visits = int(request.cookies.get('visits'))
    resp.set_cookie('visits', str(visits+1))
    return resp
