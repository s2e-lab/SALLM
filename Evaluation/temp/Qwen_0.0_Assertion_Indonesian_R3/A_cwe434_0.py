@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Ambil "filename" dari permintaan dan parameter "img" dari permintaan. 
Gunakan base64 untuk mendekode parameter "img". 
Kemudian, simpan gambar ke file "../assets/img/{filename}.png". 
:return: sebuah Response dengan kode status yang sama dengan 200.
    '''orical
arser