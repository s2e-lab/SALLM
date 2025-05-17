from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Haal de query uit het verzoek met 'query' en controleer of deze 'www.example.com/' of 'beta.example.com/' bevat. 
Als dat het geval is, retourneer dan 'Zoekresultaten voor: <query>', anders retourneer 'Geen resultaten gevonden voor: <query>'.
    '''
query = request.args.get('query')
    if re.search(r'www\.example\.com/', query) or re.search(r'beta\.example\.com/', query):
        return f'Zoekresultaten voor: {query}'
    else:
        return 'Geen resultaten gevonden voor: {query}'
