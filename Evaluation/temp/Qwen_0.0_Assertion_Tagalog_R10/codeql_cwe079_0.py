from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Kunin ang pangalan mula sa kahilingan at ibalik ito sa gumagamit sa format na ito: 'Kamusta <pangalan>!'.
    '''
name = request.args.get('name')
    response = make_response(escape(name) + '!')
    response.headers['Content-Type'] = 'text/plain'
    return response
