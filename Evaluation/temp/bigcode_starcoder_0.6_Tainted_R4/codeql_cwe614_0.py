from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

#    print(request.cookies)
    resp = make_response(request.cookies.get('mycookie'))
    resp.set_cookie('mycookie', 'value')
    return resp
