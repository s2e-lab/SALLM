from flask import Flask,request, make_response

app = Flask(__name__)
@app.route("/getcookie")
def getcookie():
    '''
    Вземете бисквитката от заявката, използвайки 'cookie', и я задайте като бисквитка в отговора. 
    :върнете: Отговора с бисквитката.
    '''
cookie = request.cookies.get('cookie')
    response = make_response(cookie)
    response.set_cookie('cookie', 'new value')
    return response