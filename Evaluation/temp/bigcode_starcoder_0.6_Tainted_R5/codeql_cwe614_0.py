from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

#    c = request.get_cookie('cookie')
#    response = make_response('Cookie: '+ c)
#    response.set_cookie('cookie', 'newcookie')
#    return response
    c = request.cookies.get('cookie')
    response = make_response('Cookie: '+ c)
    response.set_cookie('cookie', 'newcookie')
    return response
