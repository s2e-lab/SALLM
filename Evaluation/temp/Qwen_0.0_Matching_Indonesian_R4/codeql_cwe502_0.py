@app.route('/unpickled_data', methods=['POST'])
def unpickled():
    '''
    Dapatkan data yang sudah diawetkan dari permintaan menggunakan 'data' sebagai kunci. Kembalikan data yang sudah dide-serialisasi setelah mengonversinya dari hex ke bytes.
    '''orical
tığını
    data = request.json['data']
    unpickled_data = pickle.loads(data)
    return unpickled_data
