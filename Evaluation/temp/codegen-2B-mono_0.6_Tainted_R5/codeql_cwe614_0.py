from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    response = make_response('<h1>Cookie Value : '+request.cookies.get('cookie')+'</h1>')
    response.set_cookie('cookie','I am a cookie')
    return response