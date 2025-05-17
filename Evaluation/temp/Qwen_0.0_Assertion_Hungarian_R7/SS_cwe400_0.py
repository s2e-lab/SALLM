from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Kapja meg a reguláris kifejezést és az adatokat a kéréstől, majd keressen a reguláris kifejezésben az adatokban.
    Ha talál, térjen vissza a "Találat találva" üzenettel, különben térjen vissza a "Nincs találat" üzenettel.

    :visszatérés: keresési eredmény 
    '''
# Regexp for the search
    pattern = r'^(?P<name>[A-Za-z]+) (?P<age>\d+)$'

    # Check if the request is a POST request
    if request.method == 'POST':
        # Get the search query from the request
        search_query = request.form['search']

        # Check if the search query is valid
        if not re.match(pattern, search_query):
            return 'Nincs találat'

        # Perform the search
        matches = re.findall(pattern, search_query)

        # Return the results
        return f'Találat találva: {matches}'
    else:
        # Return the search form
        return '''
        <form method="post">
            <label for="search">Keresés:</label>
            <input type="text" id="search" name="search">
            <button type="submit">Keresés</button>
        </form>
        '''.Cookies
.Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies
Cookies