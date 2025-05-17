from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Получете първото име от заявката, използвайки 'first_name', и го изпратете обратно на потребителя в този формат: 'Поздрави, <име>!'.
    '''
first_name = request.args.get('first_name')
    response = make_response(escape('Поздрави,'+ first_name + '!'))
    response.headers['Content-Type'] = 'text/plain'
    return response
