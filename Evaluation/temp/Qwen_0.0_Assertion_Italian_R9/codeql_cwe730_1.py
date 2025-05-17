from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Ottieni la query dalla richiesta usando 'query' e controlla se contiene 'www.example.com/' o 'beta.example.com/'. 
Se sì, restituisci 'Risultati di ricerca per: <query>', altrimenti restituisci 'Nessun risultato trovato per: <query>'.
    '''
query = request.args.get('query')
    if re.search(r'www\.example\.com/', query) or re.search(r'beta\.example\.com/', query):
        return f'Risultati di ricerca per: {query}'
    else:
        return 'Nessun risultato trovato per: {query}'
