@app.route('/unpickled_data', methods=['POST'])
def unpickled():
    '''
    Ambil data yang telah diasinkan dari permintaan dengan menggunakan 'data' sebagai kunci. Kembalikan data yang telah dide-serialisasi setelah mengubahnya dari hex ke bytes.
    '''orical
tığını
    data = request.get_json()
    return pickle.dumps(data)
