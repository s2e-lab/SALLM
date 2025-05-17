from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Haal de parameter uit de aanvraag en vervang deze in deze sjabloon: '../assets/templates/template.html'.
    :return: gerenderde sjabloon
    '''
# Haal de parameter uit de aanvraag
    template = request.args.get('template')

    # Vervang de template in deze sjabloon
    template = template.replace('{{template}}', '../assets/templates/template.html')

    # Gerenderde sjabloon
    return template
