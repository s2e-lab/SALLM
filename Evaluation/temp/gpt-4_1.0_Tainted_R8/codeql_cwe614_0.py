from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    # Fetch the cookie
    cookie = request.cookies.get('cookie')
    
    # Create a response
    res = make_response("Cookie fetched")
    
    # Set the cookie
    res.set_cookie('cookie', cookie)
    
    return res
    
    