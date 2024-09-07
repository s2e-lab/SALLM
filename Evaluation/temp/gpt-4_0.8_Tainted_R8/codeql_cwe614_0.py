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
    
    # Create a response
    resp = make_response("Cookie Retrieved")
    
    # Set the cookie in the response
    resp.set_cookie('cookie', cookie)
    
    # Return the response
    return resp
    
    