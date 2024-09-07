from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    # Retrieve the cookie value from the request
    cookie_value = request.cookies.get('cookie')
    
    # Create a response
    response = make_response('The cookie has been read successfully.')
    
    # Set the cookie value in the response
    response.set_cookie('cookie', cookie_value)
    
    return response
    
    