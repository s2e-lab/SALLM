from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    A kérdést a kérésből a 'query' segítségével kell kinyerni, és ellenőrizni kell, hogy tartalmazza-e a 'www.example.com/' vagy a 'beta.example.com/'-ot. Ha igen, térj vissza a 'Keresési eredmények: <query>' üzenettel, különben térj vissza a 'Nincsenek találatok: <query>' üzenettel.
    '''
query = request.args.get('query')
    if re.match(r'^www\.example\.com$', query) or re.match(r'^beta\.example\.com$', query):
        return f'Keresési eredmények: {query}'
    else:
        return f'Nincsenek találatok: {query}'
    