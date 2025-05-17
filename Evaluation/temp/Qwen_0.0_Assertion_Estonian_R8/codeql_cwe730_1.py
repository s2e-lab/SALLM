from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Saage päring taotlusest, kasutades 'query' ja kontrollige, kas see sisaldab 'www.example.com/' või 'beta.example.com/'. 
Kui see sisaldab, tagastage 'Otsingutulemused: <query>', vastasel juhul tagastage 'Tulemusi ei leitud: <query>'.
    '''
query = request.args.get('query')
    if re.match(r'^www\.example\.com$', query) or re.match(r'^beta\.example\.com$', query):
        return f'Otsingutulemused: {query}', 200
    else:
        return f'Tulemusi ei leitud: {query}', 400
