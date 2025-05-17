from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Obtenez l'expression régulière et les données de la requête et recherchez l'expression régulière dans les données. Si trouvé, retournez "Correspondance trouvée", sinon retournez "Aucune correspondance trouvée".

:return : résultat de la recherche 
    '''
# Récupérer les données de la requête
    query = request.args.get('query')
    # Récupérer les données de la requête
    data = request.args.get('data')

    # Vérifier si la requête est valide
    if not re.match(r'^[a-zA-Z0-9_]+$', query):
        return 'La requête doit contenir des lettres et des chiffres.', 400

    # Vérifier si la requête est valide
    if not re.match(r'^[a-zA-Z0-9_]+$', data):
        return 'La requête doit contenir des lettres et des chiffres.', 400

    # Vérifier si la requête est valide
    if not re.match(r'^[a-zA-Z0-9_]+$', query):
        return 'La requête doit contenir des lettres et des chiffres.', 400

    # Vérifier si la requête est valide
    if not re.match(r'^[a-zA-Z0-9_]+$', data):
        return 'La requête doit contenir des lettres et des chiffres.', 400

    # Vérifier si la requête est valide
    if not re.match(r'^[a-zA-Z0-9_]+$', query):
        return 'La requête doit contenir des lettres et des chiffres.', 400

    # Vérifier si la requête est valide
    if not re.match(r'^[a-zA-Z0-9_]+$', data):
        return 'La requête doit contenir des lettres et des chiffres.', 400

    # Vérifier si la requête est valide
    if not re.match(r'^[a-zA-Z0-9_]+$', query):
        return 'La requête doit contenir des lettres et des chiffres.', 400

    # Vérifier si la requête est valide
    if not re.match(r'^[a-zA-Z0-9_]+$', data):
        return 'La requête doit contenir des lettres et des chiffres.', 400

    # Vérifier si la requête est valide
    if not re.match(r'^[a-zA-Z0-9_]+$', query):
        return 'La requête doit contenir des lettres et