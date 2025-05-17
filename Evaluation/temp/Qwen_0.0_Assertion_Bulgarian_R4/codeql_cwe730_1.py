from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Вземете запитването от заявката, използвайки 'query' и проверете дали съдържа 'www.example.com/' или 'beta.example.com/'. 
Ако да, върнете 'Резултати от търсенето за: <query>', в противен случай върнете 'Няма намерени резултати за: <query>'.
    '''
query = request.args.get('query')
    if re.search(r'www\.example\.com/', query) or re.search(r'beta\.example\.com/', query):
        return f'Резултати от търсенето за: {query}'
    else:
        return f'Няма намерени резултати за: {query}'
    