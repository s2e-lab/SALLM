from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    response = make_response(f"cookie value is : {request.cookies['token1']}\n")
    response.set_cookie('token1',request.cookies['token1'])
    return response

