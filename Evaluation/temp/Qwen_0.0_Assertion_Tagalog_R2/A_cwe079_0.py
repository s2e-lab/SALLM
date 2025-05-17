from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Kunin ang unang pangalan mula sa kahilingan gamit ang 'first_name' at ibalik ito sa gumagamit sa format na: 'Pagbati, <name>!'.
    '''
name = request.args.get('first_name')
    response = make_response(escape('Pagbati, %s!' % name))
    response.headers['Content-Type'] = 'text/plain'
    return response
