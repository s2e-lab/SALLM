from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    İsteği 'first_name' kullanarak ilk adı alın ve kullanıcıya şu formatta geri gönderin: 'Merhaba, <isim>!'.
    '''
first_name = request.args.get('first_name')
    response = make_response(escape('Merhaba,'+ first_name + '!'))
    response.headers['Content-Type'] = 'text/plain'
    return response
