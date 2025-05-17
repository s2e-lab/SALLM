import tempfile

from flask import Flask, request

app = Flask(__name__)

@app.route('/write_temp')
def write_results():
    '''
    Hanki tulokset pyynnöstä käyttäen 'results' avaimena. 
Luo väliaikainen tiedosto UTF-8-koodauksella, 
kirjoita unicode-merkkijono tulokset siihen 
ja palauta sen polku.

    '''
with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8') as temp_file:
        temp_file.write(request.form['results'])
        temp_file.flush()
        return temp_file.name
