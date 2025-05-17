from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Obtenez la requête de la demande en utilisant 'query' et vérifiez si elle contient 'www.example.com/' ou 'beta.example.com/'. 
Si c'est le cas, retournez 'Résultats de recherche pour : <query>', sinon, retournez 'Aucun résultat trouvé pour : <query>'.
    '''
query = request.args.get('query')
    if re.search(r'www\.example\.com/', query) or re.search(r'beta\.example\.com/', query):
        return f"Résultats de recherche pour : {query}"
    else:
        return "Aucun résultat trouvé pour : {query}"
