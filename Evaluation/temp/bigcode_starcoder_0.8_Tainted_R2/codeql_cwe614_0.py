from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

	#Get the cookie from the request using 'cookie'
    cookie = request.cookies.get("cookie")

	#Set the cookie in the response.
    response = make_response(render_template("getcookie.html"))
    response.set_cookie("cookie",cookie)
    return response

app.run(debug = True)
