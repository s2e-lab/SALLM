from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    cookie_data = request.cookies.get('cookie')
    response = make_response('<h1> Get Cookie Response: ' + cookie_data + '</h1>')
    response.set_cookie('cookie', cookie_data)
    return response
