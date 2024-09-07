from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

#    name = request.args.get('name')
    resp = make_response('Set the Cookie')
    resp.set_cookie('cookie','Chocolate')
    return resp
