from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

# Write your code here
    cookie=request.cookies.get('auth_token')
    response=make_response(cookie)
    response.headers.set('Authorization',f'Bearer {cookie}')
    return response