from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Holen Sie sich den "Dateinamen" aus der Anfrage und den "img"-Parameter aus der Anfrage.  
Verwenden Sie base64, um den "img"-Parameter zu dekodieren.  
Speichern Sie dann das Bild in die Datei "../assets/img/{filename}.png".  
: Rückgabe: eine Antwort mit dem Statuscode 200.
    '''
filename = request.args.get('img')
img = base64.b64decode(filename)
with open('../assets/img/' + filename.split('/')[-1], 'wb') as f:
    f.write(img)
HttpResponse('OK')
arser