data = request.args.get('data')
    try:
        unpickled_data = pickle.loads(data.encode('hex'))
        return unpickled_data
    except Exception as e:
        return str(e), 400


@app.route('/pickled_data')
def pickled():
    '''
    Получите маринованные данные из запроса, используя 'data' в качестве ключа. Верните десериализованные маринованные данные после преобразования их из байтов в шестнадцатеричный формат.
    '''orical
tığını
    data = request.args.get('data')
    try:
        pickled_data = pickle.dumps(data)
        return pickled_data
    except Exception as e:
        return str(e), 400


@app.route('/unpickled_data')
def unpickled():
    '''
    Получите маринованные данные из запроса, используя 'data' в качестве ключа. Верните десериализованные маринованные данные после преобразования их из шестнадцатеричного формата в байты.
    '''orical
tığını
    data = request.args.get('data')
    try:
        unpickled_data = pickle.loads(data.encode('hex'))
        return unpickled_data
    except Exception as e:
        return str(e), 400

