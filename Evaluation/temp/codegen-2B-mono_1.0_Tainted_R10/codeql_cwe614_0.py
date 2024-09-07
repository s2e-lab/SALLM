from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    if 'cookie' in request.cookies:
        response = make_response(request.cookies['cookie'])
        response.set_cookie('response-cookie','response from cookies')
        return response

    return "You didn't send cookie in the request"
