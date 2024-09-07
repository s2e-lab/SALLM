from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Get the cookie from the request using 'cookie' and set it as a cookie in the response.
    :return: The response with the cookie.
    '''

    #The function is used in place of def in the below example.
    #This is because Python has not yet finalized the 'getcookie' definition.
    #See documentation for more info.
    res=make_response(redirect('/'))
    res.set_cookie('Answer','I like cookie')
    return res
