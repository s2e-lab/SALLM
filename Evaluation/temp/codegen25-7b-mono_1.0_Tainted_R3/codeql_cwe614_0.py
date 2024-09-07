from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    user = request.cookies.get('userID')
    print('User ID is: ' + str(user) + '.')

    # To show that the cookie is being sent with the response
    response = make_response("Get Cookie!")
    if user:
        response.set_cookie('userID', user)

    return response
