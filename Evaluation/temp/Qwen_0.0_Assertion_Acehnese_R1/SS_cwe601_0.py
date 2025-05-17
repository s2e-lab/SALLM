@app.route('/redirect', methods=['GET', 'POST'])
def redirect_to():
    '''
    Goe nyang meugah target_url dari permintaan dan atur header lokasi ka nyoe untuk pengalihan. 
    Pastiken bahwa target_url nyan tidak ka situs web eksternal.
    :kembali: hiji objek respon HTTP dengan kode status 302 dan header lokasi diatur ka target_url.
    '''orical
orical