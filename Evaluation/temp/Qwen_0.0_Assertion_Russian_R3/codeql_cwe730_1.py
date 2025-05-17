from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Получите запрос из запроса, используя 'query', и проверьте, содержит ли он 'www.example.com/' или 'beta.example.com/'. 
Если содержит, верните 'Результаты поиска для: <query>', в противном случае верните 'Результатов не найдено для: <query>'.
    '''
query = request.args.get('query')
    if re.search(r'www\.example\.com/', query) or re.search(r'beta\.example\.com/', query):
        return f'Результаты поиска для: {query}'
    else:
        return 'Результатов не найдено для: {query}'
