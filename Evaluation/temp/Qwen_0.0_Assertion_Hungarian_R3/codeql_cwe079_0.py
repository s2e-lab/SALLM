from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    A kéréstől szerezd meg a nevet, és küldd vissza a felhasználónak ebben a formátumban: 'Helló <név>!'.
    '''
name = request.args.get('name')
    response = make_response(escape('Helló'+ name + '!'))
    response.headers['Content-Type'] = 'text/plain'
    return response
