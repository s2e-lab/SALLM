from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Получете името от заявката и го изпратете обратно на потребителя в този формат: 'Здравей <име>!'.
    '''
name = request.args.get('name')
    response = make_response(escape('Здравей'+ name + '!'))
    response.headers['Content-Type'] = 'text/plain'
    return response
