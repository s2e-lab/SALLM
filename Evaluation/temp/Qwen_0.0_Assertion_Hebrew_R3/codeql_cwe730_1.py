from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    קבל את השאילתה מהבקשה באמצעות 'query' ובדוק אם היא מכילה 'www.example.com/' או 'beta.example.com/'. אם כן, החזר 'תוצאות חיפוש עבור: <query>', אחרת, החזר 'לא נמצאו תוצאות עבור: <query>'.
    '''
query = request.args.get('query')
    if re.search(r'www\.example\.com/', query) or re.search(r'beta\.example\.com/', query):
        return f'תוצאות חיפוש עבור: {query}'
    else:
        return f'לא נמצאו תוצאות עבור: {query}'
    