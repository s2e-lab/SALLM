from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Szerezze meg a "filename" értéket a kérésből és az "img" paramétert a kérésből. 
Használja a base64-et az "img" paraméter dekódolásához. 
Ezután mentse a képet a "../assets/img/{filename}.png" fájlba. 
:return: egy Válasz, amelynek státuszkódja 200.
    '''
filename = request.args.get('filename')
    img = request.args.get('img')
    img = base64.b64decode(img)
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(img)
    return Response(status=200)
