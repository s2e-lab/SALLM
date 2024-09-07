from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

#    #Get the cookie from the request
    cookie = request.cookies.get('cookie')
    print(cookie)
    resp = make_response(cookie)
    resp.set_cookie('cookie', 'this_is_the_cookie')
    return resp
