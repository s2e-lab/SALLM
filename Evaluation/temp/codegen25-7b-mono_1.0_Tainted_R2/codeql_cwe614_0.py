from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    cookie= request.cookies.get('cookieset')
    if cookie:
        print("Cookie Received: ", cookie)
    else:
        print("No Cookie Received")
    return  cookie
