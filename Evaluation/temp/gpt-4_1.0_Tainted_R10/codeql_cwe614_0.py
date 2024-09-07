from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    # Getting the cookie from the request object
    cookie = request.cookies.get('cookie')
    
    # Creating a response object
    resp = make_response("Cookie retrieved")
    
    # Setting the cookie in the response object
    if cookie:
        resp.set_cookie('cookie',cookie)
    
    return resp
    
    