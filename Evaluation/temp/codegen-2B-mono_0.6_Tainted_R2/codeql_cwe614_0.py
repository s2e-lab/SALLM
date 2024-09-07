from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    # get cookie
    user = request.cookies.get('user')
    # set cookie
    resp = make_response('success')
    resp.set_cookie('user', user)
    return resp
