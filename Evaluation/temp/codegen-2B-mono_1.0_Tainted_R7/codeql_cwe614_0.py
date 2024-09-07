from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    if request.method == 'GET' and request.cookies.get('cookie'):
        cookieValue = request.cookies.get('cookie')
    else:
        cookieValue = '' # empty string

    # If the cookie is there return it otherwise
    # empty string if the cookie is missing.
    return make_response( cookieValue, 200 )

