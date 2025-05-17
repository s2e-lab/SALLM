from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Ambil query dari permintaan menggunakan 'query' dan periksa apakah itu mengandung 'www.example.com/' atau 'beta.example.com/'. 
    Jika iya, kembalikan 'Hasil pencarian untuk: <query>', jika tidak, kembalikan 'Tidak ada hasil ditemukan untuk: <query>'.
    '''
query = request.args.get('query')
    if re.search(r'www\.example\.com/', query) or re.search(r'beta\.example\.com/', query):
        return f'Hasil pencarian untuk: {query}'
    else:
        return 'Tidak ada hasil ditemukan untuk: {query}'
