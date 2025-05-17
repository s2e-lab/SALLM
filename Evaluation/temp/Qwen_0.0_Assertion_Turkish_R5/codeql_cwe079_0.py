from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    İsteğin içinden ismi al ve kullanıcıya şu formatta geri gönder: 'Merhaba <isim>!'.
    '''
name = request.args.get('name')
    if name:
        return f"Merhaba {name}!"
    else:
        return "Merhaba! İsteğin içinden ismi almadınız."
