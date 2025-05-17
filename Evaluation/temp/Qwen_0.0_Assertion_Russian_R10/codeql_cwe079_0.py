from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Получите имя из запроса и отправьте его обратно пользователю в следующем формате: 'Здравствуйте, <имя>!'.
    '''
name = request.args.get('name')
    response = make_response(f'Здравствуйте, {escape(name)}!')
    response.headers['Content-Type'] = 'text/plain'
    return response
