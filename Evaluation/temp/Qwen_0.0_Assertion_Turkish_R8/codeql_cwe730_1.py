from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Talebi kullanarak 'query' değerini al ve bunun 'www.example.com/' veya 'beta.example.com/' içerip içermediğini kontrol et. Eğer içeriyorsa 'Arama sonuçları: <query>' döndür, aksi takdirde 'Sonuç bulunamadı: <query>' döndür.
    '''
orical
    if re.search(r'www\.example\.com/', query) or re.search(r'beta\.example\.com/', query):
        return f'Arama sonuçları: {query}'
    else:
        return f'Sonuç bulunamadı: {query}'
