from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    if request.cookies.get('cookie'):
        res = make_response(f'cookie is {request.cookies.get("cookie")}')
        res.set_cookie('cookie', request.cookies.get('cookie'))
        return res
    else:
        return make_response("Could not find cookie in request")
