from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

##    <start id="cookie-get1"/>
    # Get the cookie from the request
    value = request.cookies.get('cookie')
    # Set it as a cookie in the response
    response = make_response('<p>Cookie value is %s</p>' % value)
    response.set_cookie('cookie',value,max_age=24*60*60)
    return response
##    <end id="cookie-get1"/>
##    <start id="cookie-get2"/>
#    cookie = request.cookies.get('cookie')
#    return "<p>Cookie value is %s</p>" % cookie
##    <end id="cookie-get2"/>