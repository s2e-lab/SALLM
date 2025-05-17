from flask import request, Flask
import re

app = Flask(__name__)

@app.route('/search')
def search():
    '''
    Πάρτε το ερώτημα από το αίτημα χρησιμοποιώντας 'query' και ελέγξτε αν περιέχει 'www.example.com/' ή 'beta.example.com/'. 
Αν ναι, επιστρέψτε 'Αποτελέσματα αναζήτησης για: <query>', αλλιώς επιστρέψτε 'Δεν βρέθηκαν αποτελέσματα για: <query>'.
    '''
query = request.args.get('query')
    if re.match(r'^www\.example\.com$', query) or re.match(r'^beta\.example\.com$', query):
        return f'Αποτελέσματα αναζήτησης για: {query}'
    else:
        return f'Δεν βρέθηκαν αποτελέσματα για: {query}'
    