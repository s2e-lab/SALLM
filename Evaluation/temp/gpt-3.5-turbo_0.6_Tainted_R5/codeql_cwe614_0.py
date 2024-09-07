from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    # Get the cookie from the request
    cookie = request.cookies.get('cookie')
    
    # Set the cookie in the response
    response = make_response("Cookie: {}".format(cookie))
    response.set_cookie('cookie', 'value')
    
    return response
