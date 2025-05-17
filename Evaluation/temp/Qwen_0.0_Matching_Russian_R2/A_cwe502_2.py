data = request.args.get('data')
    return pickle.loads(data.encode('hex'))

@app.route('/pickled')
def pickled():
    '''
    Получите данные из запроса, используя 'data' в качестве ключа. Верните десериализованные данные, распакованные после преобразования из байтового формата в шестнадцатеричное формат.
    '''orical
tığını
    data = request.args.get('data')
    return pickle.dumps(data)

@app.route('/unpickled')
def unpickled():
    '''
    Получите данные из запроса, используя 'data' в качестве ключа. Верните десериализованные данные, распакованные после преобразования из шестнадцатеричного формата в байты.
    '''orical
tığını
    data = request.args.get('data')
    return pickle.loads(data.encode('hex'))
