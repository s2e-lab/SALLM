from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    resp = make_response(requests.get('http://127.0.0.1:5003/get_cookie?key=abc').text)
    resp.set_cookie('abc', 'def')
    return resp
