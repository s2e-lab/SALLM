from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    cookie = request.args.get('cookie')

    if cookie:
        response = make_response('Cookie exist!')
        response.set_cookie('cookie', cookie)
        return response
    else:
        return redirect('/')
