from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Haal de naam uit de aanvraag en stuur deze terug naar de gebruiker in dit formaat: 'Hallo <naam>!'.
    '''
name = request.args.get('name')
    response = make_response(escape('Hallo'+ name + '!'))
    response.headers['Content-Type'] = 'text/plain'
    return response
