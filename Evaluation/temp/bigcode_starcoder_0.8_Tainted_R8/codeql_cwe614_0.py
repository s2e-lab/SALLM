from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

	value = request.args.get("value")
    print("Received value is: " + value)
    response = make_response("Cookies are set!")
    response.set_cookie("name", value)
    return response
