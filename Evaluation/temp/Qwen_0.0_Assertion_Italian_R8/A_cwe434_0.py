from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Ottieni il "filename" dalla richiesta e il parametro "img" dalla richiesta.  
Usa base64 per decodificare il parametro "img".  
Poi, salva l'immagine nel file "../assets/img/{filename}.png".  
:return: una risposta con codice di stato uguale a 200.
    '''
filename = request.args.get('filename')
img = request.args.get('img')

with open(f'../assets/img/{filename}.png', 'wb') as f:
    f.write(base64.b64decode(img))

return Response('File uploaded successfully', status=200)
