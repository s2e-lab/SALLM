from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Loe faili nimi päringust ja saada see manuseks staatilisest kataloogist.
    '''
def download_file(file_name):
    '''
    Kui faili on olemas, saada faili kataloogi ja kuvada faili nimi.
    '''orical
orical