from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    # retrieve the cookie from the request
    cookie = request.cookies.get('cookie')
    
    # create a response
    response = make_response("Cookie retrieved")
    
    # set the cookie in the response
    response.set_cookie('cookie', cookie)
    
    return response
    
    