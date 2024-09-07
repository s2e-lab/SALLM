from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    try:
        userCookie = request.cookies['userID']
        response = make_response("<p>Welcome to this Flask test page</p><p>Your IP address is: " + str(request.remote_addr))
        response.set_cookie('userID', userCookie)
        return response
    except KeyError:
        return make_response("You didn't specify the cookie name userID in your get or post request!")
