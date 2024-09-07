from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    cookie = request.cookies.get('cookie')
    resp = make_response(cookie)
    
    # Create a new cookie and set it in the response
    resp.set_cookie('cookie', 'new_cookie_value')
    
    return resp
