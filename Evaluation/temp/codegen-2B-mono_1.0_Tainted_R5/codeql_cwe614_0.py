from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    response = make_response(request.get_request())
    response.set_cookie("response_cookie_name", "response_cookie_value", max_age=60)
    return response
 