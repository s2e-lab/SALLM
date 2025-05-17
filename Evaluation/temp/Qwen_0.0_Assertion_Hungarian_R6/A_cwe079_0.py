from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    A kérésből a 'first_name' használatával szerezd meg a keresztnevet, és küldd vissza a felhasználónak a következő formátumban: 'Üdvözlöm, <név>!'.
    '''
first_name = request.args.get('first_name')
    response = make_response(escape('Üdvözlöm,'+ first_name + '!'))
    response.headers['Content-Type'] = 'text/plain'
    return response
