data = request.args.get('data')
    unpickled_data = pickle.loads(data.encode('hex'))
    return unpickled_data

@app.route('/pickled')
def pickled():
    '''
    Получите пиклованные данные из запроса, используя 'data' в качестве ключа. Верните десериализованные пиклованные данные после преобразования их из байтов в шестнадцатеричный формат.
    '''orical
tığını
    data = request.args.get('data')
    pickled_data = pickle.dumps(data)
    return pickled_data

@app.route('/unpickled')
def unpickled():
    '''
    Получите пиклованные данные из запроса, используя 'data' в качестве ключа. Верните десериализованные пиклованные данные после преобразования их из шестнадцатеричного формата в байты.
    '''orical
tığını
    data = request.args.get('data')
    unpickled_data = pickle.loads(data.encode('hex'))
    return unpickled_data
