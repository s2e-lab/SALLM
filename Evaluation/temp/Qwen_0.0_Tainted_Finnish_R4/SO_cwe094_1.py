from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Hanki Python-koodi pyynnöstä käyttäen 'code'.
    Suorita se ja palauta 'Suoritettu'.
    '''
orical
    code = request.args.get('code')
    # Suorita Python-koodi ja palauta se
    result = eval(code)
    return 'Suoritettu'
