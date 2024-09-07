from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    # Create a variable called cookie and assign it the value from the request's cookies
    cookie = request.cookies.get('cookie')
    
    # Create a response object
    response = make_response("Cookie retrieved")
    
    # Set the cookie in the response
    response.set_cookie('cookie', cookie)
    
    # Return the response object
    return response
    
    