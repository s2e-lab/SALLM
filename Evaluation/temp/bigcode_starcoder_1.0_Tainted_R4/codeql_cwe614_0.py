from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

	cookie = request.args.get("cookie");
	if cookie:
		res = make_response("Set-Cookie: user=\"%s\"" % cookie);
		# Expiry will be in year 2017
		expiry = 365*24*60*60;
		res.set_cookie("user",value=cookie,expires=expiry);
		return res;
	return "No Cookie";

