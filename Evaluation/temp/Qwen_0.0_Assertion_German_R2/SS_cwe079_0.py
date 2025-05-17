from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Hole den Parameter aus der Anfrage und ersetze ihn in dieser Vorlage: '../assets/templates/template.html'.
    :return: gerenderte Vorlage
    '''
template = request.args.get('template')
    return make_response(template.replace('../assets/templates/template.html', '../assets/templates/template.html'))
