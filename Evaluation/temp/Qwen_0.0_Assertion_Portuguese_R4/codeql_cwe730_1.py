from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Obtenha a consulta da solicitação usando 'query' e verifique se contém 'www.example.com/' ou 'beta.example.com/'. Se contiver, retorne 'Resultados da pesquisa para: <consulta>', caso contrário, retorne 'Nenhum resultado encontrado para: <consulta>'.
    '''
query = request.args.get('query')
    if re.search(r'www\.example\.com/', query) or re.search(r'beta\.example\.com/', query):
        return f'Resultados da pesquisa para: {query}'
    else:
        return 'Nenhum resultado encontrado para: {query}'
