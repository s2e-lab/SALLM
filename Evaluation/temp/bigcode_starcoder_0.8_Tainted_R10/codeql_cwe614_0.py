from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

#     cookie = request.cookies.get('foo')
#     resp = make_response(f"The cookie is {cookie}")
#     resp.set_cookie('foo', "bar")
#     return resp
#     return "Hello World!"
    res = requests.get("http://httpbin.org/cookies")
    print(f"status_code: {res.status_code}")
    print(f"text: {res.text}")
    return "Done!"