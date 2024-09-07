from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    name = request.args.get('cookie')
    response = make_response('hello')
    response.set_cookie('username', name)
    return response
