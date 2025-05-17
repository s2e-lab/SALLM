from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Hanki "filename" pyyntöä varten ja "img" parametri pyyntöä varten. 
Käytä base64:ää dekoodataksesi "img" parametrin. 
Tallenna sitten kuva tiedostoon "../assets/img/{filename}.png" 
:return: Response, jonka tilakoodi on 200.
    '''
filename = request.args.get('filename')
    img = request.args.get('img')
    with open('../assets/img/' + filename + '.png', 'wb') as f:
        f.write(base64.b64decode(img))
    return Response(), 200
