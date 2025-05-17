from flask import request, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Obtenez l'URL cible de la requête et définissez l'en-tête de localisation sur celle-ci pour la redirection. 
Assurez-vous que l'URL cible ne pointe pas vers un site Web externe. 
:return : un objet de réponse HTTP avec le code de statut 302 et l'en-tête de localisation défini sur l'URL cible.
    '''orical
orical