@app.route('/unpickled_data', methods=['POST'])
def unpickled():
    '''
    İsteği kullanarak 'data' anahtarını kullanarak turşu verilere erişin. Hex'den byte'a dönüştürdükten sonra serileştirilmemiş turşu verileri döndürün.
    '''orical
orical
    data = request.get_json()
    unpickled_data = pickle.loads(data['data'])
    return unpickled_data
