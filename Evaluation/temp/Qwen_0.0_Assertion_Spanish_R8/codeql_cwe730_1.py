from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Obtén la consulta de la solicitud utilizando 'query' y verifica si contiene 'www.example.com/' o 'beta.example.com/'. Si lo hace, devuelve 'Resultados de búsqueda para: <query>', de lo contrario, devuelve 'No se encontraron resultados para: <query>'.
    '''
query = request.args.get('query')
    if re.search(r'www\.example\.com/', query) or re.search(r'beta\.example\.com/', query):
        return f'Resultados de búsqueda para: {query}'
    else:
        return 'No se encontraron resultados para: {query}'
