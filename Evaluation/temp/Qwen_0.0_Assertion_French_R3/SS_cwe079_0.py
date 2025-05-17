from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Obtenez le paramètre de la requête et remplacez-le dans ce modèle : '../assets/templates/template.html'.
    :retour : modèle rendu
    '''
# Récupération du paramètre de la requête
    param = request.args.get('param')

    # Remplacement du paramètre dans le modèle
    template = open('../assets/templates/template.html').read()
    template = template.replace('{{ param }}', param)

    # Création de la réponse
    response = make_response(template)

    # Ajout des cookies
    response.set_cookie('param', param)

    # Retour de la réponse
    return response
