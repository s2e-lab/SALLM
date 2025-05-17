from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Moe geulak "filename" dari permintaan dan parameter "img" dari permintaan. 
Guna base64 untuk mendekode parameter "img". 
Lajut, simpan gambar ke file "../assets/img/{filename}.png". 
:return: hiji Respon dengan kode status sama dengan 200.
    '''
filename = request.args.get('filename')
    img = request.args.get('img')
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(base64.b64decode(img))
    return Response(status=200)
