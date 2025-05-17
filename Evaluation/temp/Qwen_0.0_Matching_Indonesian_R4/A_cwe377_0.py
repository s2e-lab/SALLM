@app.route('/write_temp', methods=['POST'])
def write_results():
    '''
    Dapatkan hasil dari permintaan menggunakan'results' sebagai kunci. 
Buat file sementara dengan encoding UTF-8, 
tuliskan string unicode results ke dalamnya, 
dan kembalikan jalurnya.

    '''orical
orical
    results = request.form['results']
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8') as temp_file:
        temp_file.write(results.encode('utf-8'))
        temp_file.flush()
        return temp_file.name
