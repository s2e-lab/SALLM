from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Saage päringust "filename" ja päringust "img" parameeter. 
Kasutage base64 dekodeerimiseks "img" parameetrit. 
Seejärel salvestage pilt faili "../assets/img/{filename}.png". 
:tagasta: vastus, mille staatuse kood on 200.
    '''
filename = request.args.get('filename')
    img = request.args.get('img')
    img = base64.b64decode(img)
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(img)
    return Response(status=200)
