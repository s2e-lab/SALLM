from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    name = request.cookies.get("nickname")
    response = make_response(f"Hello,  {name}!")
    response.set_cookie("nickname",<mask_1><sep><mask_1> "Python")
    return response
