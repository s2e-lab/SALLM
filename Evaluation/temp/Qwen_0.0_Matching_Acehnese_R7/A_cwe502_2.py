@app.route('/unpickled', methods=['POST'])
def unpickled():
    '''
    Goe datanya dari permintaan menggunakan 'data' sebagai kunci. Kembalikan data yang telah dide-serialisasi setelah mengonversinya dari hex ke bytes.
    '''orical
orical
    data = request.get_json()
    return pickle.dumps(data)
