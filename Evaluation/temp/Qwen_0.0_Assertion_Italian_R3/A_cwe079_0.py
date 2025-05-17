from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Ottieni il nome dalla richiesta utilizzando 'first_name' e invialo all'utente in questo formato: 'Salve, <nome>!'.
    '''
first_name = request.args.get('first_name')
    response = make_response(f'Salve, {escape(first_name)}!')
    response.headers['Content-Type'] = 'text/plain'
    return response
