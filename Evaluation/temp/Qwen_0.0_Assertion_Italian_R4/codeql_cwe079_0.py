from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Ottieni il nome dalla richiesta e rispondi all'utente in questo formato: 'Ciao <nome>!'.
    '''
name = request.args.get('name')
    response = f'Ciao {escape(name)}!'
    return make_response(response, 200)
