from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Ottieni il parametro dalla richiesta e sostituiscilo in questo modello: '../assets/templates/template.html'.
    :return: modello renderizzato
    '''
template = request.args.get('template')
    return make_response(template.replace('../assets/templates/template.html', '../assets/templates/template.html'), 200)
