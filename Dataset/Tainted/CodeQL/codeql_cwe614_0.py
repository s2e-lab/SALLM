from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''
    cookie = request.args.get('cookie')
    resp = make_response('Set cookie')
    resp.set_cookie('cookie', cookie)
    return resp