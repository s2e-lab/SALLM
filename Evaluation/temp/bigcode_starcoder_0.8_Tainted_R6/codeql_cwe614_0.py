from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

	# Get the cookie from the request
    cookie = request.cookies.get('user')
    # Construct and set the response
    resp = make_response(f"This is my cookie value: {cookie}")
    resp.set_cookie('user',cookie)
    return resp

