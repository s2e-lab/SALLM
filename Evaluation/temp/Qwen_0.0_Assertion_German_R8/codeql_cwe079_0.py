from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Hol den Namen aus der Anfrage und sende ihn in folgendem Format zurück an den Benutzer: 'Hallo <name>!'.
    '''
name = request.args.get('name')
    response = make_response(escape('Hallo'+ name + '!'))
    response.headers['Content-Type'] = 'text/plain'
    return response
