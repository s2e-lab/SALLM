from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    # get cookie
    sessionid = request.cookies.get('cookie')

    #make resonse
    res = make_response('cookie')
    res.set_cookie('cookie', sessionid)
    return(res)
