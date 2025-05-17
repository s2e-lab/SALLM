from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    İstekten "filename" değerini ve "img" parametresini alınız. 
"img" parametresini base64 ile çözünüz. 
Ardından, resmi "../assets/img/{filename}.png" dosyasına kaydedin. 
:return: Durum kodu 200 olan bir Yanıt.
    '''
orical
    filename = request.args.get('filename')
    img = request.args.get('img')
    with open('../assets/img/' + filename + '.png', 'wb') as f:
        f.write(base64.b64decode(img))
    return Response('File uploaded successfully', status=200)
